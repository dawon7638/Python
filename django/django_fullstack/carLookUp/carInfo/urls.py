from django.urls import path
from . import views




urlpatterns = [
    
    #####################GET
    path('', views.index),#landingPage
    path("dashboard", views.dashboardPage),#success page
    path("buy", views.buyPage),#buydisplay
    path("sell", views.sellPage),#selldisplay
    path("trade", views.tradePage),#tradedisplay
    path("description", views.descriptionPage),#descriptiondisplay
    path("inventory", views.inventoryPage),#inventorydisplay
    path("My_Dashboard", views.my_DashboardPage),#My_DashboardPagedisplay
    
    
    ############################ACTION
    path("register", views.register),#registration
    path("logIn", views.logIn),#logIn
    path("logged_out", views.logOut),#LogOut
    path("sellACarForm", views.sellACarForm),#sellACarForm
    path("tradeACarForm", views.tradeACarForm),#tradeACarForm
    
    
]