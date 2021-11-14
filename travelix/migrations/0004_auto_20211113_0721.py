# Generated by Django 3.2.9 on 2021-11-13 15:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('travelix', '0003_rename_recreation_area_rest_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='rest_area',
            name='from_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='rest_area',
            name='limit_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
