from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate
from django.contrib import auth
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.views import generic
from django.template.context_processors import csrf
from django.contrib.auth.models import User
from django.template import RequestContext
from django.db import IntegrityError
from useradmission.models import UserDetails,AddressDetails,PropertyDetails,PropertyImages,BidRecords,AuctionInfo,TourBooking,RentReceipt,PropertyRented
from django.contrib import messages

import datetime
from datetime import timedelta

import random
from django.core.mail import send_mail
import smtplib
from email.mime.text import MIMEText

from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from property.utils import render_to_pdf,render_to_file

from django.utils import timezone

import requests



def rented(request):
    return render(request=request, template_name='/useradmission/Templates/index.html')

def managerent(request):
    return render(request=request, template_name='regform.html')

def usermessages(request):
    return render(request=request, template_name='admission.html')
    
def myauctions(request):
    return render(request=request, template_name='index.html')


def propapplication(request):
    c1={}
    c1.update(csrf(request))
#----------------------------------- Worksection : User/Session Fetched ---------------------------------------
    sess_unm = request.session.get('unm')
    sess_pass = request.session.get('pass')
    udetails = UserDetails()
    udetails = UserDetails.objects.get(useremail=sess_unm,userpassword=sess_pass)
    
#----------------------------------- Worksection : Fetching values from FORM ----------------------------------
    pid = request.POST.get('pid','')
    print("Property id is : ", pid)

    pcat = request.POST.get('cat','')
    print("category is : ", pcat)

    rent = float(request.POST.get('rentamt',''))
    print("rent amt is : ", type(rent))

    deposit = float(request.POST.get('depoamt',''))
    print("depo amt is : ", type(deposit))

    month = int(request.POST.get('months',''))
    print("no of months is : ", type(month))

    beds = int(request.POST.get('beds',''))
    print("no of beds is : ", type(beds))

    tcat = request.POST.get('tcat','')
    print("tenant cat is : ", tcat)


    rcat = request.POST.get('rcat','')
    print("renting cat is : ", rcat)
    
    desc = request.POST.get('desc', '')
    print("description is : ", desc)

#-------------------------- Worksection : Auction Info fetch & save bid -----------------------------------
    aucprop = AuctionInfo()
    aucprop = AuctionInfo.objects.get(prop = pid)

    if (int(udetails.token)) >= (int(deposit)):
        print("token balance available : ", udetails.token)
        aucbid = BidRecords(rentbid=rent, depositbid=deposit, staybid=month,
                            bedbid=beds, personcatbid=tcat, rentingcatbid=rcat,
                            biddescription=desc, auc=aucprop, user=udetails)
        aucbid.save()
        c1 = { 'bid_success' : "You have made the bid" }
        return render(request,'tenanthome.html ',c1)
    else:
        c1 = { 'bid_success' : "Bid Unsuccessful! Insufficient Balance for Minimum Deposit"} 
        return render(request,'tenanthome.html ',c1)


def scheduletour(request):
    print("Entered Tenant section for tour booking!")
    c1={}
    c1.update(csrf(request))
    #----------------------------------- Worksection : User/Session Fetched ---------------------------------------
    sess_unm = request.session.get('unm')
    sess_pass = request.session.get('pass')
    udetails = UserDetails()
    udetails = UserDetails.objects.get(useremail=sess_unm,userpassword=sess_pass)

    #----------------------------------- Worksection : Fetching values from FORM ----------------------------------
    pid = request.POST.get('pid','')
    print("Property id : ",pid)
    pd = PropertyDetails()
    pd = PropertyDetails.objects.get(propid=pid)
    
    tourdate = request.POST.get('tourdt','')
    print("tourdate is : ",(tourdate))
    print("Type of tourdate is : ", type(tourdate))
    tourdate = datetime.strptime(tourdate, '%Y-%m-%d').date()
    print("Type of tourdate is : ", type(tourdate))

    timestart = request.POST.get('starttime','')
    print("tourtime start is : ", (timestart))
    timestart = datetime.strptime(timestart, '%H:%M:%S').time()
    print("Type of tourtime start is : ", type(timestart))

    timeend = request.POST.get('endtime','')
    print("tourtime end is : ", (timeend))
    timeend = datetime.strptime(timeend, '%H:%M:%S').time()
    print("Type of tourtime end is : ", type(timeend))

    #----------------------------------- Worksection : Creating a tour object ----------------------------------
    tb = TourBooking(
                        tourdate=tourdate, 
                        tourtimestart=timestart, 
                        tourtimeend=timeend,
                        prop=pd,
                        user=udetails
                    )
    tb.save()
    return HttpResponseRedirect('/landlord/tenant/')

def generatereceipt(request):
    print("Entered Tenant section for Receipt generation!")
    c1={}
    c1.update(csrf(request))
    sess_unm = request.session.get('unm')
    sess_pass = request.session.get('pass')
    udetails = UserDetails()
    udetails = UserDetails.objects.get(useremail=sess_unm,userpassword=sess_pass)
    #----------------------------------- Worksection : Fetching form objects ----------------------------------
    monthcount = int(request.POST.get('mcount',''))
    print("rent paid for months : ", monthcount)

    duemonth = request.POST.get('duemonth','')
    print("rent paid for the month : ", duemonth)

    prid = int(request.POST.get('prid',''))
    print("Rented id is : ", prid)

    rc = int(request.POST.get('receiptcount',''))
    print("Receipt count is : ", rc)

    pr = PropertyRented()
    pr = PropertyRented.objects.get(rentedid=prid)
    print("Property Rented object is : ", pr)
    
    tokenstopay = int( monthcount * pr.rentamount * pr.bedquantity )
    if tokenstopay <= udetails.token:
        daycount = int(31*rc)
        paymonthdate = pr.startdate + timedelta(days=daycount)
        duemonth = paymonthdate.strftime('%B')

        rentamt = pr.rentamount
        for i in range(monthcount):
            print("Rent Month is : ", duemonth)

            rr = RentReceipt(
                                amountpaid=rentamt, 
                                rentmonth=duemonth,
                                rent=pr
                            )
            rr.save()
            template = get_template('tenantinvoice.html')
            data = {
                    'propname' : str(pr.prop.propname),
                    'username' : str(udetails.userfname),
                    'month' : str(duemonth),
                    'rentpaid' : str(rentamt),
                    'time' : datetime.datetime.now().time(),
                    'date' : datetime.datetime.now().date(),
                    'transacid' : str(rr.transactionid) + "XX" + str(random.randint(1,50000)) + "XXXX"  
                    }
            file = render_to_file('tenantinvoice.html', data)
            rr.receiptpdf = file[0]
            rr.sendreceiptpermission = True
            rr.save()
            paymonthdate = paymonthdate + timedelta(days=31)
            duemonth = paymonthdate.strftime('%B') 
        print(" Tenant balance before payment : ", udetails.token)
        udetails.token = (udetails.token - tokenstopay)
        udetails.save()
        print(" Tenant balance after payment : ", udetails.token)

        ud = UserDetails()
        ud = UserDetails.objects.get(userid=pr.prop.landlord.userid)  
        print(" Landlord balance before payment : ", ud.token)
        ud.token = int(ud.token + tokenstopay)
        ud.save()
        print(" Landlord balance after payment : ", ud.token)
        c1['tkamt'] = udetails.token
        c1['errormsg'] = "Successful"
        # html = template.render(data)
        # pdf = render_to_pdf('tenantinvoice.html', data)
        # print("type of pdf after render : ", type(pdf))
        # return HttpResponse(pdf, content_type='application/pdf')
        # return HttpResponse("processsed")
        return render(request, 'collectrent.html', c1)
    else:
        c1['tkamt'] = udetails.token
        c1['errormsg'] = "Failed"
        return render(request, 'collectrent.html', c1)