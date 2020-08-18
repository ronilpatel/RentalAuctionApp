
from django.conf.urls import url
from . import views as vw

urlpatterns =[
        url('rentedpro/', vw.rented , name="rented"),
        url('managerent/', vw.managerent ,name="managerent"),
        url('messages/', vw.usermessages ,name="messages"),
        url('auctions/', vw.myauctions ,name="auctions"),
        url('apply/', vw.propapplication, name="propapplication"), 
        url('tourbooking/', vw.scheduletour, name="booktour"),
        url('generatereceipt/', vw.generatereceipt, name="receipt")
]
