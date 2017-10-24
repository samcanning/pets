from django.conf.urls import url, include


urlpatterns = [
    url(r'^', include('apps.login_app.urls')),
    url(r'^pets/', include('apps.pets_app.urls')),
]
