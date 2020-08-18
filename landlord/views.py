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
from useradmission.models import UserDetails, AddressDetails, PropertyDetails, BidRecords, AuctionInfo, PropertyRented
from django.contrib import messages
from datetime import datetime
from datetime import timedelta
import random
from django.core.mail import send_mail
import smtplib
from email.mime.text import MIMEText

  
def myhome(request):
    print("inside tenant !")
    c1={}
    c1.update(csrf(request))
    return render(request, 'tenanthome.html')

def index(request):
    sess_unm = request.session.get('unm')
    sess_pass = request.session.get('pass')
    c1={}
    c1.update(csrf(request))
    udetails = UserDetails()
    udetails = UserDetails.objects.get(useremail=sess_unm, userpassword=sess_pass)
    if udetails is not None:
        print("inside landlord :", udetails.useremail)
        return render(request,'landlordhome.html')
    else:
        HttpResponseRedirect('/useradmission/home/')

def listpro(request):
    return HttpResponseRedirect('/property/list/')    

def mybalance(request):
    c1={}
    c1.update(csrf(request))
    sess_unm = request.session.get('unm')
    sess_pass = request.session.get('pass')
    udetails = UserDetails()
    udetails = UserDetails.objects.get(useremail=sess_unm,userpassword=sess_pass)
    c1['tkamt'] = udetails.token
    return render(request, 'collectrent.html', c1)

def profile(request):
    sess_unm = request.session.get('unm')
    sess_pass = request.session.get('pass')
    c1={}
    c1.update(csrf(request))
    udetails = UserDetails()
    udetails = UserDetails.objects.get(useremail=sess_unm, userpassword=sess_pass)
    if udetails is not None:
        
        # print("user date of birth before is : ", type(df))
        # print("user date of birth before is : ", (df))

        # df = datetime.strftime(df,'%d-%m-%Y')
        # print("type of dob: ", type(df))
        # df = datetime.strptime(df,'%d-%m-%Y').date()  
        # print("user date of birth after is : ", type(df))
        # print("user date of birth after is : ", (df))
        c1['p'] = udetails
        print("mediator landed!")
        return render(request=request, template_name='testprofile.html', context=c1)
    else:
        return HttpResponseRedirect('/useradmission/home/')

def updateaccount(request):
    print("landed on main edit in views.py")
    sess_unm = request.session.get('unm')
    sess_pass = request.session.get('pass')
    c1={}
    c1.update(csrf(request))
    udetails = UserDetails()
    useraddress = AddressDetails()
    udetails = UserDetails.objects.get(useremail=sess_unm, userpassword=sess_pass)
    u = User()
    u = User.objects.get(username = sess_unm)
    print("user object : ",u.username)
    useraddress = udetails.address
    if udetails is not None:
        fname = request.POST.get('fname', '')
        udetails.userfname = fname
        print("input first name : ",fname)
        lname = request.POST.get('lname', '')
        udetails.userlname = lname
        phonenumb = request.POST.get('phonenumb','')
        print("phone number is : ",phonenumb)
        udetails.userphone = phonenumb

        user_dob = request.POST.get('udob','')
        print("Birth date is :",user_dob)
        if user_dob:
            print("type before conversion : ", type(user_dob))
            user_dob = datetime.strptime(user_dob, '%Y-%m-%d').date()
            print("type after conversion :", type(user_dob) )
            udetails.userdob = user_dob
        else:
            print("user dob not changed!")
        profileimage = request.FILES.get('propic','')
        if profileimage=='':
            print("Image not changed!")
        else:
            print("Profile photo changed !")
            udetails.userprofilephoto = profileimage
            print("profile pic url is : ", profileimage)

        gender = request.POST.get('gender','')
        udetails.usergender = gender
        category = request.POST.get('category','')
        udetails.usercategory = category
        state = request.POST.get('state1','')
        udetails.address.statename = state
        country = request.POST.get('country1','')
        useraddress.countryname = country
        pcode = request.POST.get('pcode','')
        useraddress.pincode = pcode
        c1['prochanged'] = "Profile Updated !"
        newpass = request.POST.get('newpass','')
        old_pass = request.POST.get('oldpass','')
        if newpass:
            print("Password is not blank!")
            if old_pass==(udetails.userpassword):  
                print("Password Matched !")
                udetails.userpassword = newpass
                u.set_password(newpass)
                u.save()
                c1['prochanged'] = "Password changed !"
            else:
                c1['prochanged'] = "Incorrect current password"
        print("User updated!")
        print(u.username)
        print(u.password)
        udetails.address = useraddress
        useraddress.save()
        print("user address saved!")
        udetails.save()
        c1['p'] = udetails
        print("user object saved")
        print("your profile has been saved !")
        return render(request, 'testprofile.html', c1)
    else:
        return HttpResponseRedirect('/useradmission/home/')

def updatetokenbalance(request):
    print("landed in landlord updatetoken view deffination!")
    sess_unm = request.session.get('unm')
    sess_pass = request.session.get('pass')
    c1={}
    c1.update(csrf(request))
    udetails = UserDetails()
    udetails = UserDetails.objects.get(useremail=sess_unm,userpassword=sess_pass)

    token = int(request.POST.get('tokenqty',''))
    print("Tokens to be added is : ", token)
    
    udetails.token = int(udetails.token + token)
    udetails.save()
    c1['tkamt'] = udetails.token
    print("Updated token balance is :", udetails.token)
    return render(request, 'collectrent.html', c1)