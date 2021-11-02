from django.db import models
from tinymce.models import HTMLField


class PlaceDetails(models.Model):
    title = models.CharField('Полное название места', max_length=200)
    description_short = models.TextField('Короткое описание', blank=True)
    description_long = HTMLField('Длинное описание', blank=True)
    latitude = models.FloatField('Широта')
    longitude = models.FloatField('Долгота')

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ['latitude', 'longitude']


class Place(models.Model):
    place_id = models.CharField('ID места', max_length=200, unique=True)
    title = models.CharField('Сокращенное название места', max_length=200, blank=True)
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


class Image(models.Model):
    image = models.ImageField('Изображение')
    index_number = models.IntegerField('Порядковый номер', blank=True, default=0)
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        verbose_name='К какому месту относится изображение',
        related_name='images',
        null=True,
    )

    def __str__(self):
        return f'{self.index_number} {self.place.title}'

    class Meta(object):
        ordering = ['index_number']
