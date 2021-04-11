from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    #########################
    
    path('checkout', views.checkoutForm),
    #########################
    
    path("checkout/<int:num>", views.checkoutThx),
]