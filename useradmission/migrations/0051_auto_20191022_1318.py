# Generated by Django 2.2 on 2019-10-22 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useradmission', '0050_propertydetails_messageofverify'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bidrecords',
            name='bidstatus',
            field=models.CharField(blank=True, default='pending', max_length=15, null=True),
        ),
    ]
