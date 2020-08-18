# Generated by Django 2.2 on 2019-09-12 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddressDetails',
            fields=[
                ('street1name', models.CharField(max_length=20)),
                ('street2name', models.CharField(blank=True, max_length=20, null=True)),
                ('landmark1name', models.CharField(blank=True, max_length=20, null=True)),
                ('landmark2name', models.CharField(blank=True, max_length=20, null=True)),
                ('housenumber', models.CharField(blank=True, max_length=20, null=True)),
                ('areaname', models.CharField(blank=True, max_length=20, null=True)),
                ('towncity_name', models.CharField(blank=True, max_length=20, null=True)),
                ('statename', models.CharField(blank=True, max_length=20, null=True)),
                ('countryname', models.CharField(blank=True, max_length=20, null=True)),
                ('districtname', models.CharField(blank=True, max_length=20, null=True)),
                ('buildingapartmentname', models.CharField(blank=True, max_length=20, null=True)),
                ('addressid', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='AuctionInfo',
            fields=[
                ('auctionid', models.IntegerField(primary_key=True, serialize=False)),
                ('baseprice', models.FloatField(blank=True, null=True)),
                ('startdate', models.DateField(blank=True, null=True)),
                ('enddate', models.DateField(blank=True, null=True)),
                ('starttime', models.TimeField(blank=True, null=True)),
                ('endtime', models.TimeField(blank=True, null=True)),
                ('extradetails', models.TextField(blank=True, max_length=200, null=True)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyAmenities',
            fields=[
                ('amenityid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('amenityname', models.CharField(blank=True, max_length=20, null=True)),
                ('amenityinfo', models.TextField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyDetails',
            fields=[
                ('propid', models.IntegerField(primary_key=True, serialize=False)),
                ('propname', models.CharField(blank=True, max_length=20, null=True)),
                ('propsize', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('propcategory', models.CharField(blank=True, max_length=20, null=True)),
                ('propcapacityrooms', models.IntegerField(blank=True, null=True)),
                ('propcapacitybeds', models.IntegerField(blank=True, null=True)),
                ('propavailablerooms', models.IntegerField(blank=True, null=True)),
                ('propavailablebeds', models.IntegerField(blank=True, null=True)),
                ('proprent', models.FloatField(blank=True, null=True)),
                ('propminimumstay', models.IntegerField(blank=True, null=True)),
                ('proptenantcategory', models.CharField(blank=True, max_length=20, null=True)),
                ('proprentingcategory', models.CharField(blank=True, max_length=20, null=True)),
                ('propextradetails', models.TextField(blank=True, null=True)),
                ('floornumber', models.IntegerField(blank=True, null=True)),
                ('floortotal', models.IntegerField(blank=True, null=True)),
                ('hasterrace', models.IntegerField(blank=True, null=True)),
                ('hasbalcony', models.IntegerField(blank=True, null=True)),
                ('washroomstyle', models.TextField(blank=True, null=True)),
                ('availabilitystatus', models.CharField(blank=True, max_length=10, null=True)),
                ('availablefrom', models.DateField(blank=True, null=True)),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='useradmission.AddressDetails')),
                ('amenity', models.ManyToManyField(to='useradmission.PropertyAmenities')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyRented',
            fields=[
                ('rentedid', models.IntegerField(primary_key=True, serialize=False)),
                ('dateofdeal', models.DateField(blank=True, null=True)),
                ('rentamount', models.FloatField(blank=True, null=True)),
                ('startdate', models.DateField(blank=True, null=True)),
                ('enddate', models.DateField(blank=True, null=True)),
                ('depositamount', models.FloatField(blank=True, null=True)),
                ('rentduedate', models.DateField(blank=True, null=True)),
                ('bondviolationamount', models.FloatField(blank=True, null=True)),
                ('bedquantity', models.IntegerField(blank=True, null=True)),
                ('roomquantity', models.IntegerField(blank=True, null=True)),
                ('prop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='useradmission.PropertyDetails')),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('userid', models.IntegerField(primary_key=True, serialize=False)),
                ('userfname', models.CharField(max_length=30)),
                ('userlname', models.CharField(max_length=30)),
                ('useremail', models.CharField(max_length=30)),
                ('userphone', models.CharField(blank=True, max_length=15, null=True)),
                ('userpassword', models.CharField(max_length=45)),
                ('userregdate', models.DateField(blank=True, null=True)),
                ('userprofilephoto', models.TextField(blank=True, null=True)),
                ('userdob', models.DateField(blank=True, null=True)),
                ('usergender', models.CharField(blank=True, max_length=10, null=True)),
                ('usercategory', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.ManyToManyField(to='useradmission.AddressDetails')),
            ],
        ),
        migrations.CreateModel(
            name='UserContactNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contactnumber', models.CharField(blank=True, max_length=20, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='useradmission.UserDetails')),
            ],
        ),
        migrations.CreateModel(
            name='TourBooking',
            fields=[
                ('bookingid', models.IntegerField(primary_key=True, serialize=False)),
                ('bookingdate', models.DateField(blank=True, null=True)),
                ('tourdate', models.DateField(blank=True, null=True)),
                ('tourtimestart', models.TimeField(blank=True, null=True)),
                ('tourtimeend', models.TimeField(blank=True, null=True)),
                ('currentstatus', models.CharField(blank=True, max_length=20, null=True)),
                ('prop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='useradmission.PropertyDetails')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='useradmission.UserDetails')),
            ],
        ),
        migrations.CreateModel(
            name='SearchRecords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('searchcount', models.IntegerField(blank=True, null=True)),
                ('staytime', models.TimeField(blank=True, null=True)),
                ('searchdate', models.DateField(blank=True, null=True)),
                ('searchtime', models.TimeField(blank=True, null=True)),
                ('prop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='useradmission.PropertyDetails')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='useradmission.UserDetails')),
            ],
        ),
        migrations.CreateModel(
            name='RentReceipt',
            fields=[
                ('transactionid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('rentmonth', models.CharField(blank=True, max_length=10, null=True)),
                ('dateofpayment', models.DateField(blank=True, null=True)),
                ('monthfine', models.FloatField(blank=True, null=True)),
                ('timeofpayment', models.TimeField(blank=True, null=True)),
                ('methodofpayment', models.CharField(blank=True, max_length=10, null=True)),
                ('status', models.TextField(blank=True, null=True)),
                ('rent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='useradmission.PropertyRented')),
            ],
        ),
        migrations.CreateModel(
            name='PropRooms',
            fields=[
                ('roomnumber', models.IntegerField(primary_key=True, serialize=False)),
                ('bednumber', models.IntegerField(blank=True, null=True)),
                ('bedcapacity', models.IntegerField(blank=True, null=True)),
                ('roomdetails', models.TextField(blank=True, null=True)),
                ('ismasterroom', models.BooleanField(default=True)),
                ('prop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='useradmission.PropertyDetails')),
            ],
        ),
        migrations.AddField(
            model_name='propertyrented',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='useradmission.UserDetails'),
        ),
        migrations.CreateModel(
            name='BidRecords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bidamount', models.FloatField(blank=True, null=True)),
                ('bidtime', models.TimeField(blank=True, null=True)),
                ('biddate', models.DateField(blank=True, null=True)),
                ('bidstatus', models.CharField(blank=True, max_length=15, null=True)),
                ('auc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='useradmission.AuctionInfo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='useradmission.UserDetails')),
            ],
        ),
        migrations.AddField(
            model_name='auctioninfo',
            name='prop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='useradmission.PropertyDetails'),
        ),
    ]
