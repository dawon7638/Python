from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.contrib import messages
from login_and_registration.models import User
import bcrypt, re


################################################################################

def index(request):
    if "user_id" in request.session:
        return redirect("/success")
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
    return redirect("/success")    
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
            return redirect("/success")
        
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
 
    
def successPage(request):
    if "user_id" in request.session:
        context = {
            "user": User.objects.get(id=request.session["user_id"])
        } 
        return render(request, "success.html",context)
    
    return redirect("/")
################################################################################

   
def logOut(request):
    del request.session["user_id"]
    return redirect("/")
          
          
          
       