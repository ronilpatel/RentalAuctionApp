# Generated by Django 2.2 on 2019-10-01 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('useradmission', '0029_proprooms_bedavailable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='propertydetails',
            name='picurl1',
        ),
        migrations.RemoveField(
            model_name='propertydetails',
            name='picurl2',
        ),
        migrations.RemoveField(
            model_name='propertydetails',
            name='picurl3',
        ),
        migrations.CreateModel(
            name='PropertyImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proimage', models.ImageField(blank=True, null=True, upload_to='propertypics/')),
                ('prop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='useradmission.PropertyDetails')),
            ],
        ),
    ]
