# Generated by Django 2.2 on 2019-09-17 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('useradmission', '0005_auto_20190916_2144'),
    ]

    operations = [
        migrations.RenameField(
            model_name='propertydetails',
            old_name='amenity',
            new_name='amenities',
        ),
    ]
