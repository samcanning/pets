#####[ This is the Pets_App, App level urls ]#######################################################
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.add),
    url(r'^create$', views.create),
    url(r'^user/(?P<user_id>\d+)$', views.show),
    url(r'^delete/(?P<pet_id>\d+)$', views.delete),
]