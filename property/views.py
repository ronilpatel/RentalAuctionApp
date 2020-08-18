from django.shortcuts import render
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
from useradmission.models import UserDetails,PropertyDetails,AddressDetails,PropertyAmenities,PropRooms,PropertyImages,BidRecords,AuctionInfo,PropertyRented,RentReceipt
from django.contrib import messages
import datetime
from datetime import timedelta
import random
from django.shortcuts import render
from django.core.mail import send_mail
import smtplib
from email.mime.text import MIMEText

from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from property.utils import render_to_pdf, render_to_file

from django.utils import timezone

import requests
def generate_view(request):
    template = get_template('tenantinvoice.html')
    data = {
                'date': datetime.date.today(), 
                'rentpaid': 39.99,
                'username': 'Cooper Mann',
                'transacid': 1233434,
                'month' : "December",
                'date' : datetime.datetime.now().date(),
                'time' : datetime.datetime.now().time()
            }
    file = render_to_file('tenantinvoice.html', data)
    # thread = Thread(target=send_email, args=(file,))
    # thread.start()
    # html = template.render(data)
    # pdf = render_to_pdf('tenantinvoice.html', data)
    # print("type of pdf after render : ", type(pdf))
    # return HttpResponse(pdf, content_type='application/pdf')
    return HttpResponse("processsed")
    
#_________________________________ Lander for Property Registration________ _______________________________________
def regform(request):
    c1 = {}
    c1.update(csrf(request))
    return render(request=request, template_name='registration.html', context=c1)
#__________________________________________________________________________________________________________________


#__________________________________List of property display for Landlord___________________________________________
def allprop(request):
    c1 = {}
    c1.update(csrf(request))
    #------------------------- verify session -------------------------------------------------------------------
    udetails = UserDetails()
    sess_unm = request.session.get('unm')
    sess_pass = request.session.get('pass')
    udetails = UserDetails.objects.get(useremail=sess_unm,userpassword=sess_pass)
    if udetails is not None:
        
        # ------------------- get all the properties of the landlord---------------------------------------------
        pd = PropertyDetails.objects.filter(landlord = udetails)
        print("property objects list :" ,pd)

        #-------------------- list for storing the images of property--------------------------------------------
        imglist = []       
        for j in pd: 
            print("property object :",j)
            pdimg = PropertyImages.objects.filter(prop = j)[0] # Reason for single image fetch : Thumbnail for property
            print("Image is : ",pdimg)
            print("property obj from image object is:", pdimg.prop.propname)
            imglist.append(pdimg)
        
        #---------------------Add the fetched objects to the csrf dictionary-------------------------------------
        c1['pd'] = pd
        c1['pdimg'] = imglist
        c1['landlordval'] = "landlord"
        print("list of image objects :",imglist)
        print("list of Property objects :",pd)
        print(c1)
        return render(request, 'propertylist.html',c1)
    else:
        return HttpResponseRedirect('/useradmission/signoutuser/')
#__________________________________________________________________________________________________________________




# ___________________________________Registration of property for Landlord ________________________________________
def addproperty(request):  
    udetails = UserDetails()
    sess_unm = request.session.get('unm')
    sess_pass = request.session.get('pass')
    print(sess_unm)
    print(sess_pass)
    udetails = UserDetails.objects.get(useremail=sess_unm,userpassword=sess_pass)
    print(udetails.userfname)

    if udetails is not None:

        #PROPNAME ATTRIBUTE ++++++++++++++++++++++++++++++++++++++++++++
        pname = request.POST.get('name', '')

        #PROPSIZE ATTRIBUTE ++++++++++++++++++++++++++++++++++++++++++++
        prosize = request.POST.get('sqft','')
        prosize = float(prosize)

        #PROPCATEGORY ATTRIBUTE ++++++++++++++++++++++++++++++++++++++++
        procategory = request.POST.get('pcategory','')
        print(type(procategory))

        #CAPACITYROOM ATTRIBUTE ++++++++++++++++++++++++++++++++++++++++
        roomcapacity = request.POST.get('rcapacity','')
        print("roomcapacity datatype :" ,type(roomcapacity))
        roomcapacity = int(float(roomcapacity))

        #CAPACITYBEDS ATTRIBUTE +++++++++++++++++++++++++++++++++++++++++
        # directly assigned zero
        
        #AVAILABLEROOMS ATTRIBUTE +++++++++++++++++++++++++++++++++++++++
        # directly assigned zero
                
        #AVAILABLEBEDS ATTRIBUTE ++++++++++++++++++++++++++++++++++++++++
        # directly assigned zero
        
        #RENT ATTRIBUTE +++++++++++++++++++++++++++++++++++++++++++++++++
        rent = request.POST.get('rentamt', '')
        rent = float(rent)

        #DEPOSIT ATTRIBUTE ++++++++++++++++++++++++++++++++++++++++++++++
        deposit = request.POST.get('deposit', '')
        deposit = float(deposit)

        #MINIMUMSTAY ATTRIBUTE ++++++++++++++++++++++++++++++++++++++++++
        minstay = request.POST.get('minstay','')
        minstay = int(float(minstay))
        
        #TENANTCATEGORY ATTRIBUTE +++++++++++++++++++++++++++++++++++++++
        tcat = request.POST.get('tcategory', '')
        
        #RENTINGCATEGORY ATTRIBUTE ++++++++++++++++++++++++++++++++++++++
        rcat = request.POST.get('rcategory', '')
        
        #EXTRADETAILS ATTRIBUTE +++++++++++++++++++++++++++++++++++++++++
        desc = request.POST.get('description', '')
        
        #FLOOR ATTRIBUTE ++++++++++++++++++++++++++++++++++++++++++++++++
        fnumber = 0
        ftotal = 0

        #BALCONYAVAILABLITY ATTRIBUTE++++++++++++++++++++++++++++++++++++
        balcony = request.POST.get('balcony','')
        if balcony=="Yes":
            balcony=1
        else:
            balcony=0
        balcony = int(float(balcony))

        #WASHROOM ATTRIBUTE+++++++++++++++++++++++++++++++++++++++++++++
        washroom = request.POST.get('washroom', '')

        #AVAILABLITY STATUS BYDEFAULT = 0

        #DATE FOR AVAILABLITY+++++++++++++++++++++++++++++++++++++++++++
        adate = request.POST.get('adate', '')

        #DATE FOR REGISTRATION++++++++++++++++++++++++++++++++++++++++++
        tdate = datetime.datetime.now().date()

        # ADDRESS OBJECT INFORAMATION RETRIEVAL+++++++++++++++++++++++++
        street1 = request.POST.get('s1', '')
        street2 = request.POST.get('s2', '')
        landmark1 = request.POST.get('l1', '')
        landmark2 = request.POST.get('l2', '')
        hnumber = request.POST.get('houseno', '')
        hnumber = int(float(hnumber))
        locname= request.POST.get('locality','')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        country = request.POST.get('country', '')
        district = request.POST.get('district', '')
        pcode = request.POST.get('pin', '')
        
        # AMENITIES RETRIVAL++++++++++++++++++++++++++++++++++++++++++++
        amenity = request.POST.getlist('amenities')

# ADDRESS DETAILS OBJECT STORAGE---------------------------------------------------------------------------------
        
        adddetails = AddressDetails(street1name = street1, street2name = street2, landmark1name = landmark1,
        landmark2name = landmark2, housenumber = hnumber, areaname = locname, towncity_name = city, statename = state,
        countryname = country, districtname = district , buildingapartmentname = pname, pincode = pcode)
        adddetails.save()
        print("Address details stored!")

#------------------------------------------------------------------------------------------------------------------        

# PROPERTY MODEL STORAGE---------------------------------------------------------------------------------------                

        property = PropertyDetails()
        property = PropertyDetails(propname=pname,propsize=prosize,propcategory=procategory,
        propcapacityrooms=roomcapacity,propcapacitybeds=0,propavailablerooms=0,
        proprent=rent,propdeposit=deposit,propavailablebeds=0,
        propminimumstay=minstay,proptenantcategory=tcat,proprentingcategory=rcat,
        propextradetails=desc,floornumber=fnumber,floortotal=ftotal,
        hasbalcony=balcony,washroomstyle=washroom,
        availablefrom=adate,regdate=tdate,address=adddetails, landlord=udetails)        
        property.save()

#------------------------------------------------------------------------------------------------------------------           

#this is images section---------------------------------------------------------------------------------------        

        for i in range(3):
            pimg = PropertyImages()
            imgname = "img" + str(i+1)
            imagf = request.FILES.get(imgname)
            print(f"imagefile {i+1} is {imagf}")
            pimg.proimage = imagf
            pimg.prop = property
            pimg.save()
        print("All images saved successfully!")
        property.save()

#------------------------------------------------------------------------------------------------------------------        
       
# PROPERTY AMENITIES STORAGE --------------------------------------------------------------------------------------        

        pa = PropertyAmenities()
        pa = PropertyAmenities.objects.all()
        for a in amenity:
            for pi in pa:
                print(pi.amenityname)
                if pi.amenityname==a:
                    property.amenities.add(pi) 
        property.save()
        print("Property amenities saved successfully!")
#------------------------------------------------------------------------------------------------------------------

# ROOM DETAILS MODEL STORAGE---------------------------------------------------------------------------------------
        roomnames = {}
        roomitems = []
        
        print("Total number of rooms are :", property.propcapacityrooms)
        for i in range((property.propcapacityrooms)):
            rn = "Room " + str(i+1)
            roomitems.append(rn)        
#------------------------------------------------------------------------------------------------------------------    
       
        print(roomitems)
        roomnames.update({ 'roomnumb': roomitems })
        roomnames.update({ 'prtyid': property.propid })
        print(roomnames)

        ac = AuctionInfo(baseprice=rent, prop=property, status=True)
        ac.save()
        return render(request=request, template_name='addrooms.html', context=roomnames)
    else:   
        return HttpResponseRedirect('/property/registerform/')
#__________________________________________________________________________________________________________________



#____________________________ Add individual rooms to the Property_________________________________________________

def addrooms(request):
    print("Addrooms view() reached !")
    udetails = UserDetails()
    sess_unm = request.session.get('unm')
    sess_pass = request.session.get('pass')
    print(sess_unm)
    print(sess_pass)
    udetails = UserDetails.objects.get(useremail=sess_unm,userpassword=sess_pass)
    print("Session authentication done!")
    if udetails is not None:

        # Fetching property id from url to which the rooms need to be added +++++++++++
        pid = PropertyDetails()
        pint = int(request.GET.get('q',''))
        pid = PropertyDetails.objects.get(propid=pint)
        
        # Getting the no of rooms from the property object ++++++++++++++++++++++++++++
        roomcount = pid.propcapacityrooms
        
        totalbedcount = 0
        
        # Loop for fetching individual bed counts for each room +++++++++++++++++++++++
        for i in range(roomcount):
            rn = "Room " + str(i+1)
            av = "avai" + str(i) 

            # getting no fo beds variable +++++++++++++++++++++++++++++++++++++++++++++
            beds = request.POST.get(rn,'')
            beds = int(float(beds))

            # increment bed count +++++++++++++++++++++++++++++++++++++++++++++++++++++
            totalbedcount = totalbedcount + beds

            # getting the room description ++++++++++++++++++++++++++++++++++++++++++++
            desc = request.POST.get(str(i+1),'')
           
            # creating & saving the property room objects +++++++++++++++++++++++++++++        
            pr = PropRooms(roomnumber=(i+1),bedcapacity=beds,
            roomdetails=desc,prop=pid)
            pr.save()

        # Finally reflecting total bed count to property obj by totaling it from individual room beds    
        pid.propcapacitybeds = totalbedcount
        pid.propavailablebeds = totalbedcount
        pid.save()
        print("Property finally saved!")
        return HttpResponseRedirect('/landlord/home/')
    else:
        return HttpResponseRedirect('landlord/home/')
#__________________________________________________________________________________________________________________


# ____________________________________ Single display property ____________________________________________________
def singledisplay(request):
    c1={}
    c1.update(csrf(request))
    sess_unm = request.session.get('unm')
    sess_pass = request.session.get('pass')
    udetails = UserDetails()
    udetails = UserDetails.objects.get(useremail=sess_unm,userpassword=sess_pass)
    
    #=====================objects preparation for departure to template===========================================

    # Fetching the propid from the url ++++++++++++++++++++++++
    pid = request.GET.get('q','')
    personwho = request.GET.get('cat','')
    
    if personwho=="tenant":
        checkvalue = "tenant"
    else:
        checkvalue = "landlord"
    print("Value of l is : ", )
   
    print("Property id is : ",pid)

    # Property object ready +++++++++++++++++++++++++++++++++++
    pd = PropertyDetails()
    pd = PropertyDetails.objects.get(propid = pid)
    
    # Image object ready ++++++++++++++++++++++++++++++++++++++
    imgobjs = PropertyImages.objects.filter(prop = pd)
    print("Image objs are :", imgobjs)
    for i in imgobjs:
        print("Image : ", i.proimage)

    # Room object ready +++++++++++++++++++++++++++++++++++++++
    roomobjs = PropRooms.objects.filter(prop = pd)
    print("Room objects are : ", roomobjs)
    for i in roomobjs:
        print("Room no : ", i.roomtag)

    # Amenities object ready++++++++++++++++++++++++++++++++++++
    amenityobjs = pd.amenities.all()
    print("List of all amenities is :", amenityobjs)
    
    # AuctionInfo object ready+++++++++++++++++++++++++++++++++++
    auc = AuctionInfo.objects.get(prop=pid)

    # BidRecords object ready++++++++++++++++++++++++++++++++++++
    br = BidRecords.objects.filter(auc=auc, bidstatus="pending")

    print("Bid Records are :", br)
    # Offer to Template: Objects ready++++++++++++++++++++++++++++++++++++++
    c1 = {
            'br' : br,
            'auc' : auc,   
            'pd' : pd,
            'imageobjs' : imgobjs,
            'roomobjs' : roomobjs,
            'amenityobjs' : amenityobjs,
         }
    print("Value of person who : ",checkvalue)
    if checkvalue=="landlord":
        print("I am landlord-------------------------------------------------------------")
        return render(request=request, template_name='singleproperty.html', context=c1)
    else:
        print("I am Tenant -----------------------------------------------------------")
        return render(request=request, template_name='singletenantprop.html', context=c1)    
    
#__________________________________________________________________________________________________________________


# ____________________________________ Tenant Search property List_________________________________________________
def searchfortenant(request):
    print("landed on tenant in views.py")
    sess_unm = request.session.get('unm')
    sess_pass = request.session.get('pass')
    udetails = UserDetails.objects.get(useremail=sess_unm,userpassword=sess_pass)
    #--------------------user session verified----------------------------------------
    if udetails is not None:
        c1 = {}
        c1.update(csrf(request))
        Addresultobjs = AddressDetails.objects.none()
        searchkey = request.POST.get('locationsearch','')
        print("Search key is : ", searchkey)

        #----------Fetch the relevant objects Models.py------------------------

        resultobjs1 = AddressDetails.objects.filter(areaname__contains=searchkey)
        resultobjs2 = AddressDetails.objects.filter(districtname__contains=searchkey)
        resultobjs3 = AddressDetails.objects.filter(street1name__contains=searchkey)
        resultobjs4 = AddressDetails.objects.filter(street2name__contains=searchkey)
        resultobjs5 = AddressDetails.objects.filter(towncity_name__contains=searchkey)
        resultobjs6 = AddressDetails.objects.filter(buildingapartmentname__contains=searchkey)
        resultobjs7 = AddressDetails.objects.filter(statename__contains=searchkey)
        resultobjs10 = AddressDetails.objects.filter(countryname__contains=searchkey)
        resultobjs11 = AddressDetails.objects.filter(pincode__contains=searchkey)

        #--------union of all the fetch results------------------------------------
        Addresultobjs1 = resultobjs1 | resultobjs2 | resultobjs3 | resultobjs4 | resultobjs5 | resultobjs6 | resultobjs7 | resultobjs10 | resultobjs11
        print("union is :----------- ", Addresultobjs1)
        print("---------------------------------------------------------------------")

        #-----------------------Adding the image objects----------------------------
        imglist = []       
        proplist = []
        p = PropertyDetails()
        pimg = PropertyImages()
        for j in Addresultobjs1: 
            print("Address object is : ",j)
            try:
                p = PropertyDetails.objects.get(address = j)
                proplist.append(p)
                print("property object :", p)
            except:
                print("no query matched!")
            
            print("property list : ", proplist)
            try:
                print("Property object is after save in next : ",p)
                pimg = PropertyImages.objects.filter(prop = p)[0] # Reason for single image fetch : Thumbnail for property
                imglist.append(pimg)
                print("Image is : ",pimg)
                print("property obj from image object is:", pimg.prop.propname)
            except:
                print("no query matched!")
            print("list of images :", imglist)
            
        c1['pd'] = proplist
        c1['pdimg'] = imglist
        c1['landlordval'] = "tenant"
        
        print("list of image objects : ",imglist)
        if len(proplist)==0:
            c1['nomatch'] = "NO RECORDS FOUND!"
            return render(request=request, template_name='tenanthome.html', context=c1)
        else:
            return render(request=request, template_name='showtenantresult.html', context=c1)
#__________________________________________________________________________________________________________________


# ____________________________________"approvetenant": Tenant Search property List_________________________________________________

def acceptoffer(request):
    print("Approve Tenant offer Reached !!")
    c1 = {}
    c1.update(csrf(request))
#----------------------------------- Worksection : User/Session Fetched ---------------------------------------
    sess_unm = request.session.get('unm')
    sess_pass = request.session.get('pass')
    udetails = UserDetails()
    udetails = UserDetails.objects.get(useremail=sess_unm,userpassword=sess_pass)
    
#----------------------------------- Worksection : Fetching values from FORM ----------------------------------
    bid = int(request.GET.get('q',''))
    print("Bid id is : ", bid)

    aid = int(request.GET.get('r',''))
    print("Aid id is : ", aid)

#-------------------------- Worksection : Fetching required objects -------------------------------------------
    br = BidRecords()
    br = BidRecords.objects.get(id=bid)
    print("Fetched Bid Record is : ", br)

    # pr = PropRooms.objects.filter(prop=br.auc.prop)

    tenant = UserDetails()
    tenant = UserDetails.objects.get(userid=br.user.userid)
    print("Tenant is : ", tenant.userfname)

    print("Landlord is : ", udetails.userfname)

    auction = AuctionInfo()
    auction = AuctionInfo.objects.get(auctionid=aid)
    print("Auction Record is : ", auction)

#-------------------------- Worksection : Creating PropertyRented object --------------------------------------
    pr = PropertyRented(rentamount=br.rentbid, depositamount=br.depositbid,
                        bedquantity=br.bedbid, tenantcategory=br.personcatbid,
                        rentingcategory=br.rentingcatbid, user=tenant,
                        prop=br.auc.prop)
    pr.save()
    pd = PropertyDetails()
    pd = PropertyDetails.objects.get(propid=auction.prop.propid)
    pd.availabilitystatus = False
    pd.save()
    print("Property rented object is : ", pr)

    print("Tenant account balance before deposit deduction : ", tenant.token)
    tenant.token = int(tenant.token) - int(br.depositbid)
    tenant.save()
    print("Tenant account balance after deposit deduction : ", tenant.token)

    print("Landlord account balance before deposit deduction : ", udetails.token)
    udetails.token = int(udetails.token) + int(br.depositbid)
    udetails.save()
    print("Landlord account balance after deposit deduction : ", udetails.token)

#-------------------------- Worksection : Deactivating the auction  -------------------------------------------
    auction.status = False
    auction.save()
#-------------------------- Worksection : Changing status of Bid Record------------------------------------
    br.bidstatus = "accepted"
    br.save()
    c1['successmsg'] = "Renting Deal Successful!"
    return render(request, 'landlordhome.html', c1)
#__________________________________________________________________________________________________________________
    
def pqr(request):
    print("Tenant manage property Reached !!")
    c1 = {}
    c1.update(csrf(request))
    #------------------------- verify session -------------------------------------------------------------------
    udetails = UserDetails()
    sess_unm = request.session.get('unm')
    sess_pass = request.session.get('pass')
    udetails = UserDetails.objects.get(useremail=sess_unm,userpassword=sess_pass)
    if udetails is not None:
        
        # ------------------- get all the properties of the tenant on rent---------------------------------------
        pr = PropertyRented.objects.filter(user = udetails)
        print("property objects list :" , pr)

        imglist = [] 
        for j in pr: 
            print("---------------------------************************--------------------------------------------")
            pd = PropertyDetails()
            pd = PropertyDetails.objects.get(propid = j.prop.propid)
            print("property object :", pd)
            pdimg = PropertyImages.objects.filter(prop = pd)[0] # Reason for single image fetch : Thumbnail for property
            print("Image is : ", pdimg)
            print("property obj from image object is:", pdimg.prop.propname)
            imglist.append(pdimg)
            print("---------------------------************************--------------------------------------------")
        
        #---------------------Add the fetched objects to the csrf dictionary-------------------------------------
        c1['pdimg'] = imglist
        c1['pr'] = pr
        c1['landlordval'] = "tenant"
        print("list of image objects :",imglist)
        print(c1)
        return render(request,'tenantmanageproperty.html',c1)
    else:
        return HttpResponseRedirect('/useradmission/signoutuser/')

# ____________________________________"approvetenant": Tenant Search property List_________________________________________________
def rentpayment(request):
    print("Tenant payment for rented property Reached !!")
    c1 = {}
    c1.update(csrf(request))
    #------------------------- verify session -------------------------------------------------------------------
    udetails = UserDetails()
    sess_unm = request.session.get('unm')
    sess_pass = request.session.get('pass')
    udetails = UserDetails.objects.get(useremail=sess_unm,userpassword=sess_pass)
    if udetails is not None:
        #---------------------Add the fetched objects to the csrf dictionary-------------------------------------
        pid = int(request.GET.get('q',''))
        print("Property selected is : ", pid)

        pd = PropertyDetails.objects.get(propid=pid)
        print("Property Details object is :", pd)
        
        pr = PropertyRented()
        pr = PropertyRented.objects.get(user=udetails, prop=pd)
        print("Property Rented Object is :", pr)

        # datetimeFormat = '%Y-%m-%d'
        # sdate = str(pr.startdate)
        
        # print("Type of startdate is : ", type(sdate))
        # edate = str(pr.enddate)
        # datediff = datetime.datetime.strptime(edate, datetimeFormat)-datetime.datetime.strptime(sdate, datetimeFormat)

        # diffmonths = int(datediff.days/30)

        # print("Start month name is :",pr.startdate.strftime('%B'))
        # print("End month name is :",pr.enddate.strftime('%B'))
        
        # rr = RentReceipt()

        receiptcount = int(RentReceipt.objects.filter(rent=pr).count())
        rr = RentReceipt.objects.filter(rent=pr).order_by('dateofpayment')
        daycount = int(31*receiptcount)
        print("Date after two months from start date is :", pr.startdate + timedelta(days=daycount))

        rentmonthdate = (pr.startdate + (timedelta(days=daycount)))
        print(timedelta(days=daycount))
        print("Rent to be paid month date : ", rentmonthdate)

        rentmonthtopay = rentmonthdate.strftime('%B')
        print("Rent to be paid month : ", rentmonthtopay)
        
        c1['rr'] = rr
        c1['rc'] = receiptcount
        c1['rmd'] = rentmonthdate
        c1['rid'] = pr.rentedid
        c1['rm'] = rentmonthtopay
        c1['pr'] = pr
        print(c1)
        return render(request, 'tenantpayment.html', c1)
    else:
        return HttpResponseRedirect('/useradmission/signoutuser/')
#__________________________________________________________________________________________________________________________________

    
    