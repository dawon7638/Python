from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.contrib import messages
from theWall.models import User, Message, Comment
import bcrypt, re


################################################################################

def index(request):
    if "user_id" in request.session:
        return redirect("/wall")
    return render(request, "index.html")
################################################################################


def register(request):
    print("********************Update user in dataBase function*************************")
    print(request.POST)
    errors = User.objects.basic_validator(request.POST)
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
    return redirect("/wall")    
################################################################################   
 
def logIn(request):
    print("********************Returning user function*************************")
    print(request.POST)
    errors = {}
    
    
    userObject = User.objects.filter(email_address = request.POST["email_address"])
    # userObject = userFilter.first()
    if userObject:
        logged_user = userObject[0]
        if bcrypt.checkpw(request.POST["password"].encode(), logged_user.password.encode()):
            request.session["user_id"] = logged_user.id
            return redirect("/wall")
        
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
 
    
def wallPage(request):
    if "user_id" in request.session:
        print("user_id")
        user_msg = Message.objects.all()
        user_cmt = Comment.objects.all()
        context = {
            "user": User.objects.get(id=request.session["user_id"]),
            "msg": user_msg,
            "comment": user_cmt,
        } 
        return render(request, "wall.html",context)
    
    return redirect("/")
################################################################################

   
def logOut(request):
    del request.session["user_id"]
    return redirect("/")
################################################################################          
          
          
def messageForm(request):
    ("********************MESSAGE FROM USER******************")
    print(request.POST)
    Message.objects.create(
        message = request.POST["users_messages"],
        user = User.objects.get(id=request.session["user_id"])    
    )
    return redirect("/wall")
################################################################################                    
 
    
def commentForm(request):
    ("********************COMMENT FROM USER******************")
    print(request.POST)
    Comment.objects.create(
        comment = request.POST["users_comments"],
        user = User.objects.get(id=request.session["user_id"]),
        message = Message.objects.filter()   
    )
    return redirect("/wall")
    
    
       