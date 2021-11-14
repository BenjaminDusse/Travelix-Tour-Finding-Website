# Generated by Django 3.2.9 on 2021-11-13 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelix', '0007_auto_20211113_0728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rest_area',
            name='bottom_images',
            field=models.ImageField(blank=True, null=True, upload_to='recreation_pics/bottoms'),
        ),
        migrations.AlterField(
            model_name='rest_area',
            name='image',
            field=models.ImageField(upload_to='recreation_pics/'),
        ),
        migrations.AlterField(
            model_name='review',
            name='profile_pic',
            field=models.ImageField(upload_to='reviews/'),
        ),
    ]
