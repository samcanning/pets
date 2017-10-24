#####[ This is the Login_App, App level urls ]#######################################################
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^create$', views.create),
    url(r'^logout$', views.logout),
    url(r'^welcome$', views.welcome),
]
