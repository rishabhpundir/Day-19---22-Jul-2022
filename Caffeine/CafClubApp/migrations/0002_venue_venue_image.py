# Generated by Django 3.2.4 on 2022-07-22 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CafClubApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='venue_image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
