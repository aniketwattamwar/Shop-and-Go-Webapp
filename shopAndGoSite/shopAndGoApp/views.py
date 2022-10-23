from re import L
from django.shortcuts import render
from shopAndGoApp import models
import json

import requests
session = requests.Session()

# session.get(followingurl)
# session.post(followingurl)


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

    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    password = request.POST['password']
    #Insert the details in the database. AWS boto3 RDS api
    models.insert_details(firstname, lastname, email, password)

    msg = "Account created. Please login with your account details."
    return render(request, 'login.html', {'msg': msg})

# data = json.load(open('/Users/csuftitan/Documents/Projects/Shop-and-Go-Webapp/shopAndGoSite/shopAndGoApp/data.json', 'r'))
# print(data)




def login_data(request):
    
    email = request.POST['email']
    password = request.POST['password']
    # mydata = json.dumps({'email': email,'password': password})
    # print(mydata)
    #check the entry in the database
    user_data = models.get_details()
    product_data = models.get_product_data()
    print(product_data)
    print(user_data)
    # session_data = session.post('http://127.0.0.1:8000/', data=mydata)
    # print(session_data)
    for user in user_data:
        if email == user[3] and password == user[4]:
            return render(request, 'homepage.html', {'name': user[1], 'product_data':product_data})
    
    # return render(request, "homepage.html", {'data': data})
    # return "User does not exist"

def payment(request):
    return render(request, "payment.html")

