from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User        
from django.contrib.auth import authenticate       
from django.contrib.auth import login,logout



# Home page
def home(request):
    return HttpResponse('welcome')
    # return render(request,'home.html')