from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.contrib import messages
from handy_helper.models import User, Job
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
def dashboard(request):
    job = Job.objects.all()
    
    if "user_id" in request.session:
        context = {
            "user": User.objects.get(id=request.session["user_id"]),
            "all_jobs": job,
        } 
        return render(request, "dashboard.html",context)

    return redirect("/")

# current_job = Book.objects.get(id=book_num)
#     liked_book = current_book1.uploaded_by.id
################################################################################  
def logOut(request):
    del request.session["user_id"]
    return redirect("/")
################################################################################ 
def edit_job(request, job_id):
    current_user = User.objects.get(id=request.session["user_id"])
    job = Job.objects.filter(id=job_id)
    context = {
        "user":current_user,
        "editing_job":job
    }    
    return render(request, "edit_job.html", context)

def new_job(request):
    current_user = User.objects.get(id=request.session["user_id"])
    context = {
        "user":current_user,
    }    
    
    
    return render(request, "new_job.html", context)

def job_description_page(request, job_id):
    current_user = User.objects.get(id=request.session["user_id"])
    job = Job.objects.filter(id=job_id)
    context = {
        "user": current_user,
        "all_jobs": job,
    }
    return render(request, "job_description_page.html", context)

def new_job_form(request):
    job_errors = Job.objects.job_validator(request.POST)
    if len(job_errors) > 0:
        if job_errors:
            for category, message in job_errors.items():
                messages.error(request, message)
        return redirect("/new_job")
        
    else:
        
        new_job = Job.objects.create(
            title = request.POST["title"],
            description = request.POST["description"],
            location = request.POST["location"],
            user = User.objects.get(id=request.session["user_id"]))
        return redirect("/dashboard")

def edit_job_form(request, job_id):
    job_errors = Job.objects.job_validator(request.POST)
    if len(job_errors) > 0:
        if job_errors:
            for category, message in job_errors.items():
                messages.error(request, message)
        redirect("/new_job")
        
    else:
    
        edit_job_from_list = Job.objects.get(id=job_id)
        edit_job_from_list.title = request.POST["title"]
        edit_job_from_list.description = request.POST["description"]
        edit_job_from_list.location = request.POST["location"]
        edit_job_from_list.save()
    
        return redirect("/dashboard")

def removeAJobLink(request, job_id):
    job_to_delete = Job.objects.get(id=job_id)
    print("****************REMOVING THIS JOB************")

    job_to_delete.delete()
    return redirect("/dashboard")
    



          
          
       