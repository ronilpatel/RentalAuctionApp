# Generated by Django 2.2 on 2019-09-20 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useradmission', '0016_auto_20190919_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertydetails',
            name='availabilitystatus',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='propertydetails',
            name='picurl1',
            field=models.ImageField(blank=True, null=True, upload_to='propertypics/'),
        ),
        migrations.AlterField(
            model_name='propertydetails',
            name='picurl2',
            field=models.ImageField(blank=True, null=True, upload_to='propertypics/'),
        ),
        migrations.AlterField(
            model_name='propertydetails',
            name='picurl3',
            field=models.ImageField(blank=True, null=True, upload_to='propertypics/'),
        ),
    ]
