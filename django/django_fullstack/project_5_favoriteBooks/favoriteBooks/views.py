from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.contrib import messages
from favoriteBooks.models import User, Book
import bcrypt, re


################################################################################
def index(request):
    if "user_id" in request.session:
        return redirect("/books")
    return render(request, "index.html")
################################################################################
def register(request):
    errors = User.objects.user_validator(request.POST)
    print("********************Update user in dataBase function*************************")
    print(request.POST)
    if len(errors) > 0:
        print("*"*87)
        if errors:
            for category, message in errors.items():
                messages.error(request, message)
        redirect("/")
        
    else:
        hashed_pw = bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt()).decode()
        print("#"*87)
        print(hashed_pw)
        new_user = User.objects.create(
            first_name = request.POST["first_name"], 
            last_name =  request.POST["last_name"], 
            email_address = request.POST["email_address"], 
            password = hashed_pw,
        )
        request.session["user_id"] = new_user.id
    return redirect("/books")    
################################################################################   
def logIn(request):
    errors = {}
    print("********************Returning user function*************************")
    print(request.POST)
   
    userObject = User.objects.filter(email_address = request.POST["email_address"])
    # userObject = userFilter.first()
    if userObject:
        logged_user = userObject[0]
        if bcrypt.checkpw(request.POST["password"].encode(), logged_user.password.encode()):
            request.session["user_id"] = logged_user.id
            return redirect("/books")
        
        else:
            errors["password"] = "Oops try again!"
            
            for key, value in errors.items():
                messages.warning(request, value)                
            return redirect("/")
        
    else:
        errors["email_address"] = "Oops try again!"
        
        for key, value in errors.items():
            messages.warning(request, value)                
        return redirect("/")  
################################################################################        
def dashboard(request):
    current_user_id = User.objects.get(id=request.session["user_id"])
    books_on_list = Book.objects.all()
    if "user_id" in request.session:
        # ("*************************ADDING BOOKS TO PAGE*************************")
        context = {
            "user": User.objects.get(id=request.session["user_id"]),
            "all_books_on_list": Book.objects.all(),
        }
        print(request.POST) 
        return render(request, "dashBoard.html",context)
    
    return redirect("/")
################################################################################   
def logOut(request):
    del request.session["user_id"]
    return redirect("/")
################################################################################
def updateBook(request, book_num):
    books = Book.objects.filter(id=book_num)
    context = {
        "updating_books":books
    }
    return render(request, "updateBook.html", context)         
################################################################################
def readOne(request, book_num):
    current_user_id = User.objects.get(id=request.session["user_id"])
    books = Book.objects.filter(id=book_num)
    current_book1 = Book.objects.get(id=book_num)
    liked_book = current_book1.uploaded_by.id
    # current_liked_book = Book.objects.get(id=book_num)
    # current_user_id.uploaded_by.remove(id=book_num)
    
    
    
    print("Im the current user")
    print(current_user_id)
    
    context = {
        "users_liked_list": books,
        "user": current_user_id,
        "current_liked_book": liked_book,
        "book_num": book_num,
        
        
    }
    return render(request, "readOne.html", context)         
################################################################################
def unFavoriteABookLink(request, book_id):
    book_to_UnFavoriteList = Book.objects.get(id=book_id)
    print("****************UNFAVORITING THIS BOOK************")
    print(book_to_UnFavoriteList)
    logged_in = User.objects.get(id=request.session["user_id"])
    print("****************UNFAVORITING THIS BOOK/LOGGED IN************")
    print(logged_in)
    book_to_UnFavoriteList.users_who_like.remove(logged_in)
    return redirect("/books")
################################################################################
def updateABookForm(request, book_id):
    book_errors = {}
    print("*************************UPDATING BOOKS FORM*************************")
    print(request.POST)
    
    updated_current_liked_book = Book.objects.get(id=book_id)
    updated_current_liked_book.title = request.POST["title"]
    updated_current_liked_book.desc = request.POST["desc"]
    # uploaded_by = User.objects.get(id=request.session["user_id"])
    updated_current_liked_book.save()
    return redirect("/books")        
################################################################################
def addABookForm(request):
    book_errors = {}
    print("*************************ADDING BOOKS FORM*************************")
    print(request.POST)
    
    newly_created_book = Book.objects.create(
    title = request.POST["title"],
    desc = request.POST["desc"],
    uploaded_by = User.objects.get(id=request.session["user_id"]))
    print(newly_created_book.title)
    
    return redirect("/books")         
################################################################################
def deleteABookLink(request, book_id):
    book_to_delete = Book.objects.get(id=book_id)
    print("****************DELETING THIS BOOK************")

    book_to_delete.delete()
    return redirect("/books")
################################################################################
def addAFavoriteBookLink(request, book_id):
    book_to_addToFavoriteList = Book.objects.get(id=book_id)
    print("****************FAVORITING THIS BOOK************")
    print(book_to_addToFavoriteList)
    logged_in = User.objects.get(id=request.session["user_id"])
    book_to_addToFavoriteList.users_who_like.add(logged_in)
    return redirect("/books")
################################################################################    
          
          
       