# Generated by Django 3.2.9 on 2021-11-14 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelix', '0010_auto_20211113_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='rest_area',
            name='rating_stars',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]