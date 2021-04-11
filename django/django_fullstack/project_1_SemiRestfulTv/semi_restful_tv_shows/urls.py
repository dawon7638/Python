from django.urls import path
from . import views

urlpatterns = [
    path("shows", views.read_all),
    ###############################
    
    path("shows/new", views.create),
    path("shows_added", views.createForm),
    #######################################
    
    path("shows/<int:num>", views.read_one),
    ##########################################
    
    path("shows/<int:num>/edit", views.update),
    path("show_edited",views.updateForm),
    ###############################################
    
    # path("/shows/<int:num>/destroy", views.destroy)
    
]