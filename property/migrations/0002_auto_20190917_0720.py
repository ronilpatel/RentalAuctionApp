# Generated by Django 2.2 on 2019-09-17 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertydetails',
            name='prodeposit',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='propertydetails',
            name='regdate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='propertydetails',
            name='availabilitystatus',
            field=models.CharField(blank=True, default='unavailable', max_length=10, null=True),
        ),
    ]
