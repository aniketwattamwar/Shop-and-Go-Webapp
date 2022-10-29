from django.urls import path

from . import views

urlpatterns = [
        
        path('',views.home, name = 'home'),
        path('homepage',views.login_data, name = 'homepage'),
        path('login', views.login, name = 'login'),
        path('signup',views.signup, name = 'signup'),
        path('register',views.get_data),
        path('payment',views.payment),
        path('logout',views.logout),
        path('address',views.address),
        path('addpayment',views.addpayment),
        path('review',views.review)
        ]

