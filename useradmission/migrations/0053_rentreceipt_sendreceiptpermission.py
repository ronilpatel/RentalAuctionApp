# Generated by Django 2.2 on 2019-10-23 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useradmission', '0052_rentreceipt_receiptpdf'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentreceipt',
            name='sendreceiptpermission',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]