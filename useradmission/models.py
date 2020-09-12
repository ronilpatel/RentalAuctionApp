from django.db import models
from django.utils import timezone
from django.db.models.signals import post_delete, post_save, pre_delete

# from easy_pdf.rendering import render_to_pdf
from django.core.mail import send_mail
import smtplib
import os
from email.mime.text import MIMEText
from django.conf import settings
import random

from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
# from property.utils import render_to_pdf, render_to_file
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 



from django.utils import timezone

# import requests

# pdfurl = str(settings.BASE_DIR) + "/media/receiptpdfs/"

# print("final url is : ", pdfurl)

class AddressDetails(models.Model):
    street1name = models.CharField(max_length=20)
    street2name = models.CharField(max_length=20, blank=True, null=True)
    landmark1name = models.CharField(max_length=20, blank=True, null=True)
    landmark2name = models.CharField(max_length=20, blank=True, null=True)
    housenumber = models.CharField(max_length=20, blank=True, null=True)
    areaname = models.CharField(max_length=20, blank=True, null=True)
    towncity_name = models.CharField(max_length=20, blank=True, null=True)
    statename = models.CharField(max_length=20, blank=True, null=True)
    countryname = models.CharField(max_length=20, blank=True, null=True)
    districtname = models.CharField(max_length=20, blank=True, null=True)
    buildingapartmentname = models.CharField(max_length=20, blank=True, null=True)
    pincode = models.CharField(max_length=10, blank=True, null=True)
    addressid =  models.AutoField(primary_key=True)

class UserDetails(models.Model):
    userid =  models.AutoField(primary_key=True)
    userfname = models.CharField(max_length=30)
    userlname = models.CharField(max_length=30)
    useremail = models.CharField(max_length=30, unique=True)
    userphone = models.CharField(max_length=15, blank=True, null=True)
    userpassword = models.CharField(max_length=45)
    userregdate = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    userprofilephoto = models.ImageField(upload_to="profiles/",blank=True,null=True)
    userdob = models.DateField(blank=True, null=True)
    usergender = models.CharField(max_length=10, blank=True, null=True)
    usercategory = models.CharField(max_length=15, blank=True, null=True)
    token = models.IntegerField(blank=True, null=True, default=0)

    address = models.OneToOneField('AddressDetails', on_delete=models.CASCADE, null=True)

class PropertyDetails(models.Model):
    propid =  models.AutoField(primary_key=True)
    propname = models.CharField(max_length=20, blank=True, null=True)
    propsize = models.FloatField(blank=True, null=True)
    propcategory = models.CharField(max_length=20, blank=True, null=True)
    propcapacityrooms = models.IntegerField(blank=True, null=True)
    propcapacitybeds = models.IntegerField(blank=True, null=True)
    propavailablerooms = models.IntegerField(blank=True, null=True)
    propavailablebeds = models.IntegerField(blank=True, null=True)
    proprent = models.FloatField(blank=True, null=True)
    propdeposit = models.FloatField(blank=True, null=True)
    propminimumstay = models.IntegerField(blank=True, null=True)
    proptenantcategory = models.CharField(max_length=20, blank=True, null=True)
    proprentingcategory = models.CharField(max_length=20, blank=True, null=True)
    propextradetails = models.TextField(blank=True, null=True)
    floornumber = models.IntegerField(blank=True, null=True)
    floortotal = models.IntegerField(blank=True, null=True)
    hasbalcony = models.IntegerField(blank=True, null=True)
    washroomstyle = models.CharField(max_length=10,blank=True, null=True)
    availabilitystatus = models.BooleanField(max_length=15, default=False)
    verifystatus = models.BooleanField(max_length=15, default=False)
    availablefrom = models.DateField(blank=True, null=True)
    regdate = models.DateField(auto_now_add=True, null=True, blank=True)
    messageofverify = models.TextField(blank=True, null=True, default="Hello")
    
    address = models.OneToOneField('AddressDetails', on_delete=models.CASCADE)
    landlord = models.ForeignKey('UserDetails', on_delete=models.CASCADE, null=True)
    amenities = models.ManyToManyField('PropertyAmenities')

# def before_delete_post(sender,instance,**kwargs):
#     ud = UserDetails()
#     ud = instance.landlord
#     FROM_EMAIL = ""
#     PASSWORD = ""
#     try:
#         gmail = smtplib.SMTP('smtp.gmail.com',587)
#         gmail.ehlo()
#         gmail.starttls()
#         gmail.login(FROM_EMAIL,PASSWORD)
#     except:
#         print("Email Setup Failed!")
#     t = "Hey " + str(ud.userfname) + "! Your Property has failed the verification process" + "\n"
#     t = t + "\n\n" + str(instance.messageofverify)
#     msg = MIMEText(t)
#     msg['Subject'] = 'Rental Auction Verification!'
#     msg['To'] = ud.useremail
#     msg['From'] = FROM_EMAIL
    
#     try:
#         gmail.send_message(msg)
#         print("Email sent successfully")
#     except:
#         print("Failed to send email!")

# pre_delete.connect(before_delete_post, sender=PropertyDetails)

class PropertyImages(models.Model):
    proimage = models.ImageField(upload_to="propertypics/",blank=True,null=True)
    prop = models.ForeignKey('PropertyDetails', on_delete=models.CASCADE)

class PropertyAmenities(models.Model):
    amenityid = models.CharField(max_length=20, primary_key=True)
    amenityname = models.CharField(max_length=20, blank=True, null=True)
    amenityinfo = models.TextField(max_length=50, blank=True, null=True)

class PropRooms(models.Model):

    roomnumber = models.AutoField(primary_key=True)
    roomtag = models.IntegerField(blank=True, null=True, default=1)
    bedcapacity = models.IntegerField(blank=True, null=True)
    bedavailable = models.IntegerField(blank=True, null=True)
    roomdetails = models.TextField(blank=True, null=True)
    ismasterroom = models.BooleanField(default=False)

    prop = models.ForeignKey('PropertyDetails',on_delete=models.CASCADE)


class PropertyRented(models.Model):
    
    rentedid = models.AutoField(primary_key=True)
    dateofdeal = models.DateField(auto_now_add=True, blank=True, null=True)
    timeofdeal = models.TimeField(auto_now_add=True, blank=True, null=True)
    rentamount = models.FloatField(blank=True, null=True)
    startdate = models.DateField(blank=True, null=True)
    depositamount = models.FloatField(blank=True, null=True)
    staymonthcount = models.IntegerField(blank=True,null=True,default=6)
    bondviolationamount = models.FloatField(blank=True, null=True)
    bedquantity = models.IntegerField(blank=True, null=True)
    tenantcategory = models.CharField(max_length=10, blank=True, null=True)
    rentingcategory = models.CharField(max_length=10, blank=True, null=True)
    
    user = models.ForeignKey('UserDetails', on_delete=models.CASCADE)
    prop = models.ForeignKey('PropertyDetails',on_delete=models.CASCADE)


class RentReceipt(models.Model):
    
    transactionid = models.AutoField(primary_key=True)
    amountpaid = models.IntegerField(null=True, blank=True)
    rentmonth = models.CharField(max_length=10, blank=True, null=True)
    dateofpayment = models.DateField(auto_now_add=True,blank=True, null=True)
    monthfine = models.FloatField(blank=True, null=True,default=0)
    timeofpayment = models.TimeField(auto_now_add=True, blank=True, null=True)
    methodofpayment = models.CharField(max_length=10, blank=True, null=True, default="token")
    sendreceiptpermission = models.BooleanField(null=True, blank=True, default=False)
    receiptpdf = models.FileField(upload_to='receiptspdf/', null=True, blank=True)
    
    rent = models.ForeignKey('PropertyRented',on_delete=models.CASCADE)

def after_save_post(sender,instance,**kwargs):
    if instance.sendreceiptpermission:
        ud = UserDetails()
        ud = instance.rent.user

        # template = get_template('tenantinvoice.html')
        # data = {
        #         'username' : str(ud.userfname),
        #         'month' : str(instance.rentmonth),
        #         'rentpaid' : str(instance.amountpaid),
        #         'time' : str(instance.timeofpayment),
        #         'date' : str(instance.dateofpayment),
        #         'transacid' : str(instance.transactionid) + "XX" + str(random.randint(1,50000)) + "XXXX"  
        #         }
        # file = render_to_file('tenantinvoice.html', data)
        # instance.receiptpdf = file[0]
        # instance.save()

        FROM_EMAIL = ""
        TO_EMAIL = str(ud.useremail)
        PASSWORD = ""
        try:
            gmail = smtplib.SMTP('smtp.gmail.com', 587)
            gmail.ehlo()
            gmail.starttls()
            gmail.login(FROM_EMAIL, PASSWORD)
        except:
            print("Email Setup Failed!")
        t = "Hey " + str(ud.userfname) + "! This is an instance of Rent Receipt \n\n"
        t = t + " Rent Month : " + str(instance.rentmonth) + "\n" 
        t = t + " Rent Paid  : " + str(instance.amountpaid) + "\n" 
        t = t + " Date of Payment : " + str(instance.dateofpayment) + "\n" 
        t = t + " Time of Payment : " + str(instance.timeofpayment) + "\n" 
        t = t + " Method of Payment : " + str(instance.methodofpayment) + "\n" 
        msg = MIMEMultipart()
        body = MIMEText(t, 'plain')
        msg['Subject'] = 'Rent Receipt - ' + str(instance.rentmonth)
        msg['To'] = ud.useremail
        msg['From'] = FROM_EMAIL
        msg.attach(body)

        filename = str(instance.receiptpdf)
        file_path = os.path.join(settings.MEDIA_ROOT, "receiptspdf/" + filename)
        print("complete filepath of pdf is : ", file_path)
        attachment = open(file_path, "rb")

        p = MIMEBase('application', 'octet-stream') 
        p.set_payload((attachment).read()) 
        encoders.encode_base64(p) 
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
        msg.attach(p) 
        text = msg.as_string() 
        try:
            gmail.sendmail(FROM_EMAIL, TO_EMAIL,text)
            print("Email sent successfully")
        except:
            print("Failed to send email!")
        
post_save.connect(after_save_post, sender=RentReceipt)


class AuctionInfo(models.Model):
    
    auctionid = models.AutoField(primary_key=True)
    baseprice = models.FloatField(blank=True, null=True)
    startdate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)
    starttime =  models.TimeField(blank=True, null=True)
    endtime =  models.TimeField(blank=True, null=True)
    extradetails = models.TextField(max_length=200, null=True, blank=True)
    status = models.BooleanField(default=False)

    prop = models.ForeignKey('PropertyDetails',on_delete=models.CASCADE)


class BidRecords(models.Model):

    rentbid = models.FloatField( blank=True, null=True)
    depositbid = models.FloatField( blank=True, null=True)
    staybid = models.IntegerField( blank=True, null=True, default=0)
    bedbid = models.IntegerField( blank=True, null=True, default=0)
    personcatbid = models.CharField( max_length=10, blank=True, null=True)
    rentingcatbid = models.CharField( max_length=10, blank=True, null=True)
    biddescription = models.TextField(max_length=100, blank=True, null=True)
    bidtime = models.TimeField(auto_now_add=True,  blank=True, null=True)
    biddate = models.DateField (auto_now_add=True, blank=True, null=True)
    bidstatus = models.CharField(max_length=15, blank=True, null=True, default="pending")
    
    auc = models.ForeignKey('AuctionInfo', on_delete=models.CASCADE)
    user = models.ForeignKey('UserDetails', on_delete=models.CASCADE)
       

class SearchRecords(models.Model):

    searchcount = models.IntegerField(blank=True, null=True)
    staytime = models.TimeField(blank=True, null=True)
    searchdate = models.DateField(auto_now_add=True, blank=True, null=True)
    searchtime = models.TimeField(auto_now_add=True, blank=True, null=True)

    user = models.ForeignKey('UserDetails', on_delete=models.CASCADE)
    prop = models.ForeignKey('PropertyDetails', on_delete=models.CASCADE)


class TourBooking(models.Model):

    bookingid = models.AutoField(primary_key=True)
    bookingdate = models.DateField(auto_now_add=True, blank=True, null=True)
    tourdate = models.DateField(blank=True, null=True)
    tourtimestart = models.TimeField(blank=True, null=True)
    tourtimeend = models.TimeField(blank=True, null=True)
    currentstatus = models.BooleanField(blank=True, null=True, default=False)
    
    prop = models.ForeignKey('PropertyDetails', on_delete=models.CASCADE)
    user = models.ForeignKey('UserDetails', on_delete=models.CASCADE)


class UserContactNumber(models.Model):
    contactnumber = models.CharField(max_length=20, blank=True, null=True)
    user = models.ForeignKey('UserDetails', on_delete=models.CASCADE)
