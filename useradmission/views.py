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
from useradmission.models import UserDetails,PropertyDetails
from django.contrib import messages
import datetime
import random
import string
from django.core.mail import send_mail
import smtplib
from email.mime.text import MIMEText

def index(request):
    return render(request=request, template_name='index.html', context={})

def signup(request):
    c1 = {}
    c1.update(csrf(request))
    return render(request=request, template_name='admission.html', context=c1)

def sign(request):
    fname = request.POST.get('fname', '')
    lname = request.POST.get('lname', '')
    useremail = request.POST.get('uemail','')
    # password1 = request.POST.get('pass1','')

    def pw_gen(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
	    return ''.join(random.choice(chars) for _ in range(size))

    psize = random.randint(7,15)
    password1 = pw_gen(int(psize))
    print(password1)
    secret_key = b'1234567890123467890'
    tdate = datetime.date.today()    
    print("information collected")    
    details =  UserDetails(userfname = fname, userlname = lname, useremail = useremail, userpassword = password1, userregdate = tdate)
    details.save()
    print("userdetails stored!")
    uname = useremail
    u = User(username = uname)
    u.set_password(password1)
    u.save()
    print("User listed")
    print(u.username)
    print(u.password)
    #the password will be sent to the user's email by using smtp protocol
    FROM_EMAIL="rentalauctions@gmail.com"
    PASSWORD="rentalauction143"
    try:
        gmail = smtplib.SMTP('smtp.gmail.com',587)
        gmail.ehlo()
        gmail.starttls()
        gmail.login(FROM_EMAIL,PASSWORD)
    except:
        print("Email Setup Failed!")
    t = "Hey " + str(fname) + "! We are Happy to have you. Your password is : " + password1 +" Make sure you login!"
    msg=MIMEText(t)
    msg['Subject'] = 'Rental Auction Verification'
    msg['To'] = useremail
    msg['From'] = FROM_EMAIL
    try:
        gmail.send_message(msg)
    except:
        print("Failed to send email!")
    return HttpResponseRedirect('/useradmission/login/')

def login(request):
    c = {}
    c.update(csrf(request))
    return render(request=request, template_name='admission.html', context=c)

def auth_view(request):        
    username = request.POST.get('uemail', '')
    password = request.POST.get('upassword', '')
    try:
        user = auth.authenticate(username = username, password = password)
        print("user authenticated!")
    except KeyError:
        return render(request, 'admission.html', {'login_message' : 'Fill in all fields',}) 
   
    if user is not None:
        print("user is found!!")
        request.session["unm"]=username
        ud = UserDetails.objects.get(useremail=username)
        request.session["pass"]=ud.userpassword
        auth.login(request, user)
        print("logged in!")
        print(request.session.get('unm'))
        return HttpResponseRedirect('/landlord/home/')
    else:
        return render(request,'admission.html', {'login_message' : 'Please enter valid credentials'})

def contact(request):
    return render(request=request, template_name='contact.html')

def about(request):
    return render(request=request, template_name='about.html')

def signoutuser(request):
    if request.session.get('unm') is not None:
        del request.session['unm']
        del request.session['pass']
        auth.logout(request)
        return HttpResponseRedirect('/useradmission/home/')
    else:
        return HttpResponseRedirect('/useradmission/login/')