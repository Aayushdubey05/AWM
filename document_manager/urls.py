from django.urls import path
from django.urls import path, include
#from django.conf.urls import url
#from core.views import *
from . import views

#setting the url partters for the viewa

urlpatterns = [
    path('',views.Documents.as_view(), name='documents'), 
]