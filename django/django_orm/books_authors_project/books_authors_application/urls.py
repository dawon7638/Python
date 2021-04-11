from django.urls import path
from . import views

urlpatterns = [
    
    #Books
    path('', views.index),
    path("addBook", views.addBook),
    path("books/<int:viewNum>", views.bookDesc),
    path("addAuthorsBook", views.bookDescAddAuthor),
    
    #Authors
    path("author", views.addAuthorIndex),
    path("addAuthor", views.addAuthor),
    path("author/<int:AuthorId>", views.authorNote),
    path("addBooksAuthor", views.authorNoteAddBook),
]