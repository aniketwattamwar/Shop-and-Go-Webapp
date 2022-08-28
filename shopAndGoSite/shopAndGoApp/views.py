from django.shortcuts import render
from django.http import HttpResponse
from wsgiref.util import FileWrapper
from django import forms

from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    return render(request,"index.html")

# def login(request):
#     return render(request,"login.html")

# def signup(request):
#     return render(request,"Signup.html")

def get_data(request):

    email = request.POST['email']
    return render(request, 'index.html', {'email': email})




