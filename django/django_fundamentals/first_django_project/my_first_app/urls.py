from django.urls import path     
from . import views 



urlpatterns = [
    path("blogs", views.myblog),
    path("blogs/new", views.new),
    path("blogs/create", views.goback),
    path("", views.create),
    path("blogs/<int:nums>", views.show),	   
    path("blogs/<int:nums>/edit", views.edit),
    path("blogs/<int:nums>/delete", views.destroy)	   
]

