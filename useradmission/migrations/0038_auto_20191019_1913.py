# Generated by Django 2.2 on 2019-10-19 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useradmission', '0037_proprooms_roomtag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctioninfo',
            name='auctionid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='propertyrented',
            name='rentedid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='proprooms',
            name='roomnumber',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='rentreceipt',
            name='transactionid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
