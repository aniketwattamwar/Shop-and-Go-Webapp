from itertools import product
from re import L
from django.shortcuts import render
from shopAndGoApp import models
import json
import requests

# session.get(followingurl)
# session.post(followingurl)
sess = {}
# Create your views here.
def home(request):
    return render(request,"index.html")

def login(request):
    return render(request, "login.html")    

def signup(request):
    return render(request,"Signup.html")

def get_data(request):

    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    password = request.POST['password']
    #Insert the details in the database. AWS boto3 RDS api
    models.insert_details(firstname, lastname, email, password)

    msg = "Account created. Please login with your account details."
    return render(request, 'login.html', {'msg': msg})

def login_data(request):
    # flag = 0
    email = request.POST['email']
    password = request.POST['password']
    #check the entry in the database
    user_data = models.get_details(password)
    # sess = request.session.get('user',user_data) 
    request.session['user'] = user_data
    product_data = models.get_product_data()
    
    if request.session['user']:
        return render(request, 'homepage.html', {'name': user_data[0][1],'product_data': product_data})
    

def logout(request):

    # sess_name = request.session.get('session_data', sess)
    # del request.session['user']
    msg = "Logged out"
    try:
        del request.session['user']
    except KeyError:
        pass
    return render(request,'index.html')

def payment(request):

    return render(request, "payment.html")


def address(request):

    adr1 = request.POST['adr1']
    adr2 = request.POST['adr2']
    address = adr1 + adr2
    print(address)
    user_id = 1
    order_id = 1
    product_id = 1
    models.insert_address(user_id,address,order_id,product_id)
    adr_msg = "Address Added"
    return render(request,'payment.html',{'adr_msg': adr_msg})

def addpayment(request):
    name = request.POST['name']
    cardnumber = request.POST['cardnumber']
    # expiry = request.POST['expiry']
    user_id = 1
    order_id = 2
    amount = 399
    models.add_payment(user_id, amount, order_id, name, cardnumber)
    pay_msg = "Card details added!\n Proceed to Pay now."
    return render(request, 'payment.html',{'pay_msg': pay_msg})



def review(request):
    review = []
    user_id = 1
    product_id = 1
    address = models.get_address(user_id)
    payment = models.get_payment(user_id)
    ordered_product = models.get_ordered_product(product_id)
    

    return render(request,'payment.html',{'address':address,'payment':payment,'ordered_product':ordered_product})



