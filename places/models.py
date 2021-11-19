from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField('Название места', max_length=200, blank=True)
    description_short = models.TextField('Короткое описание', blank=True)
    description_long = HTMLField('Длинное описание', blank=True)
    latitude = models.FloatField('Широта')
    longitude = models.FloatField('Долгота')

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ['latitude', 'longitude']


class Image(models.Model):
    image = models.ImageField('Изображение')
    index_number = models.IntegerField('Порядковый номер', blank=True, default=0)
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        verbose_name='К какому месту относится изображение',
        related_name='images',
    )

    def __str__(self):
        return f'{self.index_number} {self.place.title}'

    class Meta(object):
        ordering = ['index_number']
