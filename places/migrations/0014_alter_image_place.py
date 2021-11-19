# Generated by Django 3.2.7 on 2021-11-19 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0013_remove_place_place_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='place',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='places.place', verbose_name='К какому месту относится изображение'),
            preserve_default=False,
        ),
    ]