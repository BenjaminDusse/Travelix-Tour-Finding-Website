# Generated by Django 3.2.8 on 2021-11-18 02:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelix', '0033_auto_20211117_1805'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='rest_area',
            options={'ordering': ['date_created'], 'verbose_name': 'Rest_area', 'verbose_name_plural': 'Rest_areas'},
        ),
    ]
