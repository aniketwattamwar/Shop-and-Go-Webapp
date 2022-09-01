from django.shortcuts import render
from django.http import HttpResponse
from wsgiref.util import FileWrapper
from django import forms

from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    return render(request,"index.html")

def login(request):
    return render(request, "login.html")

def signup(request):
    return render(request,"Signup.html")

# def homepage(request):
#     return render(request,"homepage.html")

def get_data(request):

    email = request.POST['email']
    password = request.POST['password']
    #Insert the details in the database. AWS boto3 RDS api

    msg = "Account created. Please login with your account details."
    return render(request, 'login.html', {'msg': msg})

def login_data(request):

    email = request.POST['email']
    password = request.POST['password']
    #check the entry in the database 
    
    return render(request, 'homepage.html', {'email': email})



