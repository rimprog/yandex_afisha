# Generated by Django 3.2.7 on 2021-11-19 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0014_alter_image_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Название места'),
        ),
    ]