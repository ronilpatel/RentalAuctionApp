# Generated by Django 2.2 on 2019-09-16 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useradmission', '0004_auto_20190916_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertydetails',
            name='picurl1',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='propertydetails',
            name='picurl2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='propertydetails',
            name='picurl3',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='userprofilephoto',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]