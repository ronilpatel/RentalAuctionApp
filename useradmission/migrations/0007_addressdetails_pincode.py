# Generated by Django 2.2 on 2019-09-17 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useradmission', '0006_auto_20190917_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='addressdetails',
            name='pincode',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
