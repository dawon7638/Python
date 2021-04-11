from django.urls import path
from . import views




urlpatterns = [
    
    #####################GET
    path('', views.index),#logIn/RegisterPagee(render)
    path("books", views.dashboard),#dashboardpage(render)
    # path("books/<int:book_num>/edit", views.updateBook),#updateBookpage(render)
    path("books/<int:book_num>", views.readOne),#readOneDescriptionPage(render)
    
    
    
    ############################ACTION
    path("register", views.register),#registration Form
    path("logIn", views.logIn),#logIn Form
    path("updateABookForm/<int:book_id>",views.updateABookForm),#updateBookForm
    path("addABookForm", views.addABookForm),#addABookForm
    path("logged_out", views.logOut),#logOut hyperlink
    path("unFavoriteABookLink/<int:book_id>", views.unFavoriteABookLink),#Unfavorite Book hyperlink
    path("deleteABookLink/<int:book_id>", views. deleteABookLink),#Delete a book hyperlink
    path("addAFavoriteBookLink/<int:book_id>", views.addAFavoriteBookLink),
    
    
]