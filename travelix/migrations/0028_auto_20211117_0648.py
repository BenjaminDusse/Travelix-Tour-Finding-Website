# Generated by Django 3.2.8 on 2021-11-17 14:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('travelix', '0027_alter_rest_area_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('profile_pic', models.ImageField(upload_to='reviews/')),
                ('content', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='rest_area',
            name='review',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.AddField(
            model_name='comment',
            name='rest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='travelix.rest_area'),
        ),
    ]
