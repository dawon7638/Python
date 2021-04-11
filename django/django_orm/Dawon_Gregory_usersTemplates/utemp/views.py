from django.shortcuts import render, redirect

from utemp.models import user
# Create your views here.

def index(request):
    users = user.objects.all()
    print("*"*87)
    print(users)
    
    context = {
        "users": users
    }
    return render(request, "index.html", context)



def hello(request):
    
    user1 = user.objects.create(userfirst = request.POST["userfirst"], userlast = request.POST["userlast"], useremail = request.POST["useremail"], userage = request.POST["userage"])
    
    return redirect("/")


