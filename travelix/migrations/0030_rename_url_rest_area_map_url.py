# Generated by Django 3.2.8 on 2021-11-17 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelix', '0029_comment_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rest_area',
            old_name='url',
            new_name='map_url',
        ),
    ]