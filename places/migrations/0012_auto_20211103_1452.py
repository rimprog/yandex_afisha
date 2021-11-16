# Generated by Django 3.2.7 on 2021-11-03 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0011_auto_20211103_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.CharField(blank=True, max_length=200, verbose_name='Название места'),
        ),
        migrations.AlterUniqueTogether(
            name='place',
            unique_together={('latitude', 'longitude')},
        ),
        migrations.RemoveField(
            model_name='place',
            name='place_details',
        ),
        migrations.RemoveField(
            model_name='place',
            name='title_place_details',
        ),
        migrations.DeleteModel(
            name='PlaceDetails',
        ),
    ]