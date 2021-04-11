from django.urls import path
from . import views




urlpatterns = [
    ##################LOGIN/REGISTRATION###########################
    
    #####################GET#################################
    path('', views.index),#login/registration page
    path("logged_out", views.logOut),#Hyperlink for log out
    
    ####################ACTION###############################
    path("register", views.register),#registration form
    path("logIn", views.logIn),#logIn form
    
    ##################THE WALL######################################
    
    #####################GET#################################
    path("wall", views.wallPage),#wall page
    
    ####################ACTION###############################
    path("add_message", views.messageForm),#New message form
    path("add_comment", views.commentForm),#New comment form
    
    
    
]