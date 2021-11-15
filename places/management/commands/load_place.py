from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from places.models import Place, Image

import requests


class Command(BaseCommand):
    help = 'Loads places to database from URL contains json. \
    URL Example: https://bit.ly/3qzRT1b'

    def add_arguments(self, parser):
        parser.add_argument('place_url', type=str)

    def handle(self, *args, **options):
        url = options['place_url']

        response = requests.get(url)
        response.raise_for_status()

        payload = response.json()

        place, is_place_created = Place.objects.get_or_create(
            title = payload['title'],
            latitude = payload['coordinates']['lat'],
            longitude = payload['coordinates']['lng'],
            defaults = {
                'description_short': payload['description_short'],
                'description_long': payload['description_long'],
            }

        )
        self.stdout.write(self.style.SUCCESS(f'Successfully {"created" if is_place_created else "get"} Place object "{place.title}"'))

        for image_index, image_url in enumerate(payload['imgs'], 1):
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
