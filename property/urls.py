from django.conf.urls import url
from . import views as vw

urlpatterns = [
    url('list/', vw.regform, name="regform"),
    url('registerform/', vw.addproperty, name="addproperty"),
    url('addrooms/', vw.addrooms, name="addrooms"),
    url('manage/', vw.allprop , name='allprop'),
    url('singleproperty/', vw.singledisplay, name="singledisplay"),
    url('searchprop/', vw.searchfortenant, name="searchfortenant"),
    url('approvetenant/', vw.acceptoffer, name="acceptoffer"),
    url('pay/', vw.pqr, name="managetenant"),
    url('rentpayment/', vw.rentpayment, name="rentpayment"),
    url('getreceipt/', vw.generate_view, name="genreceipt")
]