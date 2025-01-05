from django.shortcuts import render
from . import models 
from django.http import HttpResponse

# Create your views here.

def home(response):
    return HttpResponse("Welcome to the Automated Writing Machine (AWM)!")