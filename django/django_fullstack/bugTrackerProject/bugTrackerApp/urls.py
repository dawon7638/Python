from django.urls import path
from . import views




urlpatterns = [
    
    #####################GET
    path('', views.index),#landingPage
    path("dashboard", views.dashboard),#dashboard page
    
    
    ############################ACTION
    path("register", views.register),#registration
    path("logIn", views.logIn),#logIn
    path("logged_out", views.logOut),
    
]