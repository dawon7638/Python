from django.urls import path
from . import views




urlpatterns = [
    
    #####################GET
    path('', views.index),#landingPage
    path("dashboard", views.dashboard),#success page
    path("edit_job/<int:job_id>", views.edit_job),#edit_job page
    path("new_job", views.new_job),#new_job page
    path("job_description_page/<int:job_id>", views.job_description_page),#job_description_page
    
    
    
    ############################ACTION
    path("register", views.register),#registration
    path("logIn", views.logIn),#logIn
    path("new_job_form", views.new_job_form),#new_job_form
    path("edit_job_form", views.logIn),#edit_job_form
    path("logged_out", views.logOut),#html link
    path("removeAJobLink/<int:job_id>", views.removeAJobLink),#Delete a book hyperlink
    
]