from django.urls import path
from . import views




urlpatterns = [
    
    #####################GET
    path('', views.index),#landingPage
    path("success", views.successPage),#success page
    
    
    ############################ACTION
    path("register", views.register),#registration
    path("logIn", views.logIn),#logIn
    path("logged_out", views.logOut),
    
]