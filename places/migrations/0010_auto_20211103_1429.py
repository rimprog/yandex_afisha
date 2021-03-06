# Generated by Django 3.2.7 on 2021-11-03 11:29

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0009_alter_place_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Длинное описание'),
        ),
        migrations.AddField(
            model_name='place',
            name='description_short',
            field=models.TextField(blank=True, verbose_name='Короткое описание'),
        ),
        migrations.AddField(
            model_name='place',
            name='title_place_details',
            field=models.CharField(blank=True, max_length=200, verbose_name='Полное название места'),
        ),
    ]
