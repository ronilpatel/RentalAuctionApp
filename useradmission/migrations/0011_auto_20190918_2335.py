# Generated by Django 2.2 on 2019-09-18 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useradmission', '0010_auto_20190917_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertydetails',
            name='hasbalcony',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
