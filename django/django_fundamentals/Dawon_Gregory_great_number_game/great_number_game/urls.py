from django.urls import path     
from . import views







urlpatterns = [
    path('', views.index),
    path("process_form",views.pagetwo),
    path("cookiemonster", views.destroy)
]