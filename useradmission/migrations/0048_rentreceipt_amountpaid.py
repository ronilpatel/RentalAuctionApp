# Generated by Django 2.2 on 2019-10-20 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useradmission', '0047_auto_20191021_0224'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentreceipt',
            name='amountpaid',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
