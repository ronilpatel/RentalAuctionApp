# Generated by Django 2.2 on 2019-09-29 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useradmission', '0026_remove_propertydetails_propcapacityrooms'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertydetails',
            name='propcapacityrooms',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]