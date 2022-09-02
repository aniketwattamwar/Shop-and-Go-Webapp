from django.shortcuts import render
from shopAndGoApp import models


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

def login_data(request):

    email = request.POST['email']
    password = request.POST['password']
    #check the entry in the database
    user_data = models.get_details()
    print(user_data)
    for user in user_data:
        if email == user[3] and password == user[4]:
            return render(request, 'homepage.html', {'name': user[1]})
    
    return "User does not exist"


