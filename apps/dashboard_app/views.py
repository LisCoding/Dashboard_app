from django.shortcuts import render, HttpResponse, redirect
from django.contrib.messages import error
import bcrypt
from models import *

def index(request):
    return render(request,'dashboard_app/index.html')

def signin(request):
    return render(request,'dashboard_app/signin.html')

def register(request):
    return render(request,'dashboard_app/register.html')
