from django.shortcuts import render, redirect
from dojo_ninja_shell.models import dojos, ninjas

def index(request):
    dojo = dojos.objects.all()
    ninja = ninjas.objects.all()

    context = {
        "all_dojos" : dojo,
        "all_ninjas" :ninja
    }
    # curr_dojo = dojos.objects.get(id=dojo.id)
    return render(request, "index.html", context)
    

def add_dojos(request):
    print("*"*87)
    print(request.POST)
    
    
    dojos.objects.create(name = request.POST["name"], city = request.POST["city"], state = request.POST["state"])
     
    return redirect("/")
            

def add_ninjas(request):
    print("*"*87)
    print(request.POST)
    
    dojo = dojos.object.get(id=request.POST["dojos"])
    
    ninjas.objects.create(first_name = request.POST["first_name"], last_name = request.POST["last_name"], edojos = dojo)
    
    return render(request, "index.html")
    
    # # print(user2)
    # return render(request, "index.html")






