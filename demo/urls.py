from django.conf.urls import url
from . import views

urlpatterns = [
    
    url(r'^secure$', views.secure, name='secure'),
    url(r'^$', views.dashboard, name = 'dashboard'),
]