# Generated by Django 3.2.8 on 2021-11-18 04:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_social_network'),
    ]

    operations = [
        migrations.AddField(
            model_name='social_network',
            name='soc_net_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.social_network'),
        ),
    ]
