# Generated by Django 2.2 on 2019-10-20 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useradmission', '0040_auto_20191020_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourbooking',
            name='currentstatus',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
