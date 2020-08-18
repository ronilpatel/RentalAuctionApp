from django.conf.urls import url
from . import views as vw

urlpatterns = [
    url('home/', vw.index, name='index'),

    url('signup/', vw.signup, name='signup'),

    url('login/', vw.login, name='login'),

    url('contact/', vw.contact, name='contact'),

    url('about/', vw.about, name='about'),

    url('sign/', vw.sign, name='sign'),

    url('auth/',vw.auth_view, name='auth_view'),

    url('signoutuser/', vw.signoutuser, name='signoutuser'),
]