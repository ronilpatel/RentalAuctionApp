# Generated by Django 2.2 on 2019-10-22 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useradmission', '0051_auto_20191022_1318'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentreceipt',
            name='receiptpdf',
            field=models.FileField(blank=True, null=True, upload_to='receiptspdf/'),
        ),
    ]