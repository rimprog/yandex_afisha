# Generated by Django 3.2.7 on 2021-11-03 11:29

from django.db import migrations


def move_place_details_to_place(apps, schema_editor):
    PlaceDetails = apps.get_model('places', 'PlaceDetails')

    for place_details in PlaceDetails.objects.all():
        place = place_details.place
        place.title_place_details = place_details.title
        place.description_short = place_details.description_short
        place.description_long = place_details.description_short

        place.save()


def move_backward(apps, schema_editor):
    PlaceDetails = apps.get_model('places', 'PlaceDetails')

    for place_details in PlaceDetails.objects.all():
        place = place_details.place
        place.title_place_details = ''
        place.description_short = ''
        place.description_long = ''

        place.save()


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0010_auto_20211103_1429'),
    ]

    operations = [
        migrations.RunPython(move_place_details_to_place, move_backward)
    ]
