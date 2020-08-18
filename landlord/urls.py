from django.conf.urls import url
from . import views as vw

urlpatterns = [
    url('home/', vw.index, name='index'),
    url('tenant/', vw.myhome, name='myhome'),
    url('list/', vw.listpro , name='list'),
    url('showbalance/', vw.mybalance , name='collect'),
    url('profile/', vw.profile , name='profile'),
    url('updateaccount/', vw.updateaccount , name='updateuserprofile'),
    url('addtokens/', vw.updatetokenbalance, name="addtokens"),
]