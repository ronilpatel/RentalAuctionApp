# Generated by Django 2.2 on 2019-10-20 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useradmission', '0039_auto_20191019_1914'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='propertyrented',
            name='enddate',
        ),
        migrations.RemoveField(
            model_name='propertyrented',
            name='roomquantity',
        ),
        migrations.AddField(
            model_name='propertyrented',
            name='rentingcategory',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='propertyrented',
            name='tenantcategory',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='propertyrented',
            name='timeofdeal',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
    ]