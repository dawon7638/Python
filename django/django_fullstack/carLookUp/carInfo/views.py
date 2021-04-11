from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.contrib import messages
from carInfo.models import User, Vehicle
import bcrypt, re


################################################################################
def index(request):
    if "user_id" in request.session:
        return redirect("/dashboard")
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
    return redirect("/dashboard")    
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
            return redirect("/dashboard")
        
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
def dashboardPage(request):
    seller = User.objects.all()
    if "user_id" in request.session:
        context = {
            "user": User.objects.get(id=request.session["user_id"]),
            "all_customers": seller,
        } 
        return render(request, "dashboard.html",context)
    
    return redirect("/")
################################################################################
def buyPage(request):
    current_user = User.objects.get(id=request.session["user_id"])
    context = {
        "user":current_user,
    }   
    
    return render(request, "buyPage.html", context)
################################################################################
def sellPage(request):
    current_user = User.objects.get(id=request.session["user_id"])
    context = {
        "user":current_user,
    }   
    return render(request, "sellPage.html", context)
################################################################################
def sellACarForm(request):
    car_errors = Vehicle.objects.car_validator(request.POST)
    if len(car_errors) > 0:
        if car_errors:
            for category, message in car_errors.items():
                messages.error(request, message)
        return redirect("/sell")
        
    else:
        
        sell_vehicle = Vehicle.objects.create(
            year = request.POST["year"],
            make = request.POST["make"],
            model= request.POST["model"],
            vin= request.POST["vin"],
            mileage= request.POST["mileage"],
            note= request.POST["note"],
            user = User.objects.get(id=request.session["user_id"]))
        return redirect("/dashboard")
################################################################################
def tradePage(request):
    current_user = User.objects.get(id=request.session["user_id"])
    context = {
        "user":current_user,
    }   
    return render(request, "tradePage.html", context)
################################################################################   
def tradeACarForm(request):
    car_errors = Vehicle.objects.car_validator(request.POST)
    if len(car_errors) > 0:
        if car_errors:
            for category, message in car_errors.items():
                messages.error(request, message)
        return redirect("/sell")
        
    else:
        
        sell_vehicle = Vehicle.objects.create(
            year = request.POST["year"],
            make = request.POST["make"],
            model= request.POST["model"],
            vin= request.POST["vin"],
            mileage= request.POST["mileage"],
            note= request.POST["note"],
            user = User.objects.get(id=request.session["user_id"]))
    return(redirect, "dashboard")
################################################################################
def descriptionPage(request):
    current_user = User.objects.get(id=request.session["user_id"])
    context = {
        "user":current_user,
    }   
    return render(request, "descriptionPage.html", context)
################################################################################
def inventoryPage(request):
    current_user = User.objects.get(id=request.session["user_id"])
    context = {
        "user":current_user,
    }   
    return render(request, "inventoryPage.html", context)
################################################################################
def my_DashboardPage(request):
    current_user = User.objects.get(id=request.session["user_id"])
    context = {
        "user":current_user,
    }   
    return render(request, "customerDashboardPage.html", context)
################################################################################
def logOut(request):
    del request.session["user_id"]
    return redirect("/")
################################################################################
          
          
       