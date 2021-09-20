from django.db import models


class PlaceDetails(models.Model):
    title = models.CharField('Полное название места', max_length=200)
    description_short = models.CharField('Короткое описание', max_length=400)
    description_long = models.TextField('Длинное описание')
    latitude = models.FloatField('Широта')
    longitude = models.FloatField('Долгота')

    def __str__(self):
        return self.title


class Place(models.Model):
    place_id = models.CharField('ID места', max_length=200)
    title = models.CharField('Сокращенное название места', max_length=200)
    latitude = models.FloatField('Широта')
    longitude = models.FloatField('Долгота')
    place_details = models.OneToOneField(
        PlaceDetails,
        on_delete=models.SET_NULL,
        verbose_name='Сведения о месте',
        related_name='place',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title
