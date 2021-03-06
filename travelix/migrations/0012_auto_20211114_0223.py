# Generated by Django 3.2.9 on 2021-11-14 10:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('travelix', '0011_rest_area_rating_stars'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rest_area',
            name='rating_stars',
        ),
        migrations.AlterField(
            model_name='rest_area',
            name='dislikes',
            field=models.ManyToManyField(blank=True, null=True, related_name='post_dislikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='rest_area',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, related_name='post_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
