# Generated by Django 2.2 on 2019-10-19 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useradmission', '0035_auto_20191019_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertydetails',
            name='regdate',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='propertyrented',
            name='dateofdeal',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='rentreceipt',
            name='timeofpayment',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='searchrecords',
            name='searchdate',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='searchrecords',
            name='searchtime',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='tourbooking',
            name='bookingdate',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='userregdate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
