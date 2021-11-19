# Generated by Django 3.2.8 on 2021-11-17 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelix', '0022_rename_client_client_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='rest_area',
            name='url',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to=''),
        ),
    ]