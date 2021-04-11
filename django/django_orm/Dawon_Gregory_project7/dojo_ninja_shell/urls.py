from django.urls import path
from . import views








urlpatterns = [
    path('', views.index),
    path("process_forn", views.add_ninjas),
    path("process_form", views.add_dojos),
]