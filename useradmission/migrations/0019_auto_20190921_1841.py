# Generated by Django 2.2 on 2019-09-21 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useradmission', '0018_auto_20190921_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='userregdate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
