from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from books_authors_application.models import Author, Book

#######################################################
def index(request):
    book = Book.objects.all()
    print("*************ALL OF BOOKS****************")
    
    print(book)
    context = {
        "all_books":book
        }
    return render(request,"bookspage1.html", context)

    print("*************ALL OF BOOKS****************")

########################################################
def addBook(request):# Adds the books on the root page
    print("****************PROCESSING BOOKS**************")
    
    print(request.POST)
    Book.objects.create(title = request.POST["title"], desc = request.POST["desc"])
    return redirect("/")

    print("****************PROCESSING BOOKS**************")
    
#########################################################
def bookDesc(request,viewNum):#Sends user to description page
    print("***********GETTING BOOKS/DESCRIPTIONS FROM VIEWS BUTTON****************")
    
    book = Book.objects.get(id=viewNum)
    current_book = book
    author = Author.objects.exclude(books=book)
    print("***************************")
    print(author)
    print("***************************")
    context = {
        "all_books":book,
        "current_book": book,
        "all_authors":author,
        "writers":book.authors.all()
        }
    
   
    # print(author)
    return render(request,"bookspage2.html", context)

    print("***********GETTING BOOKS/DESCRIPTIONS VIEWS FORM****************")

########################################################
def bookDescAddAuthor(request):
    print("")
    print("*************ADDING AUTHORS TO BOOK DESCRIPTIONS****************")
    print(request.POST)
    
    
    
    return redirect(f"books/{request.POST['current_book']}")

    print("*************ADDING AUTHORS TO BOOK DESCRIPTIONS****************")

########################################################
def addAuthorIndex (request):# Adds the authors on the root page
    author = Author.objects.all()
    print("*************ALL AUTHORS****************")
    print(author)
    
    context = {
        "all_authors": author
        }   
    return render(request,"authorspage1.html", context)
    

    print("*************ALL AUTHORS****************")
    
    ########################################################
def addAuthor(request):# Adds the books on the root page
    print("****************PROCESSING AUTHORS**************")

    print(request.POST)
    Author.objects.create(first_name = request.POST["first_name"], last_name = request.POST["last_name"], note = request.POST["note"])
    

    print("****************PROCESSING AUTHORS**************")
    return redirect("authorspage1.html")
    ########################################################  
def authorNote(request,AuthorId):#Sends user to note page
    print("***********GETTING AUTHOR/NOTES FROM VIEWS BUTTON****************")
    
    author = Author.objects.get(id=AuthorId)
    current_author = author
    book = Book.objects.exclude(authors=author)
    # print(author.note)
    context = {
    "all_books": book,
    "current_author": author,
    "all_authors":author,
    "writers":author.books.all()
    }
    
    return render(request,"authorspage2.html", context)



    print("***********GETTING AUTHOR/NOTES FROM VIEWS BUTTON****************")
    
    ########################################################
    
def authorNoteAddBook(request):#Authors note page
    print("")
    print("*************ADDING BOOKS TO AUTHORS NOTES****************")
    print(request.POST)
    
    return redirect(f"authors/{request.POST['current_author']}")

    print("*************ADDING BOOKS TO AUTHORS NOTES****************")
    
    
    