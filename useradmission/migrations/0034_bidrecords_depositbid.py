# Generated by Django 2.2 on 2019-10-19 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useradmission', '0033_auto_20191019_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='bidrecords',
            name='depositbid',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
