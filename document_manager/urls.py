from django.urls import path

from . import views

#setting the url partters for the viewa

urlpatterns = [
    path('', views.home, name='home'),
]