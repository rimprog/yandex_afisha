from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from places.models import Place, PlaceDetails, Image

import requests


class Command(BaseCommand):
    help = 'Loads places to database from URL contains json. URL Example: https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%90%D0%BD%D1%82%D0%B8%D0%BA%D0%B0%D1%84%D0%B5%20Bizone.json'

    def add_arguments(self, parser):
        parser.add_argument('place_url', type=str)

    def handle(self, *args, **options):
        url = options['place_url']

        response = requests.get(url)
        response.raise_for_status()

        place_json = response.json()

        place_details, is_place_details_created = PlaceDetails.objects.get_or_create(
            latitude = place_json['coordinates']['lat'],
            longitude = place_json['coordinates']['lng'],
            defaults = {
                'title': place_json['title'],
                'description_short': place_json['description_short'],
                'description_long': place_json['description_long'],
            }
        )
        self.stdout.write(self.style.SUCCESS(f'Successfully {"created" if is_place_details_created else "get"} PlaceDeatails object "{place_details.title}"'))

        place, is_place_created = Place.objects.get_or_create(
            place_id = str(place_details.latitude) + str(place_details.longitude),
            defaults = {
                'title': place_details.title,
                'latitude': place_details.latitude,
                'longitude': place_details.longitude,
                'place_details': place_details
            }
        )
        self.stdout.write(self.style.SUCCESS(f'Successfully {"created" if is_place_created else "get"} Place object "{place.title}"'))

        for image_index, image_url in enumerate(place_json['imgs'], 1):
            response = requests.get(image_url)
            response.raise_for_status()

            image_binary = response.content
            image_name = image_url.split('/')[-1]

            image, is_image_created = Image.objects.get_or_create(
                index_number = image_index,
                place = place,
            )
            if is_image_created:
                image.image.save(image_name, ContentFile(image_binary), save=True)
                self.stdout.write(self.style.SUCCESS(f'Successfully {"created" if is_image_created else "get"} Image object "{image}"'))
