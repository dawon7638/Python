from django.shortcuts import render, HttpResponse, redirect 
import random

# Create your views here.







    
def index(request):
    actualnum = random.randint(1,100)
    request.session["actualnum"] = actualnum
    print("*"*87)
    return render(request, 'index.html')
    
    
    
     
    
    



def pagetwo(request):
    print(request.POST)
    actualnum = request.session["actualnum"]
    
    if request.POST["usernum"] == "":
        print("Seriously?!")
        return render(request, "tryagain.html")
    
    request.session["usernum"] = int(request.POST["usernum"])
     
    if request.session["usernum"] >= 100:
        print("Seriously?!")
        return render(request, "tryagain.html")
    
    elif request.session["usernum"]  > actualnum: 
        print ("Too high!")
        return render(request, "high.html")
    
    elif request.session["usernum"] <= 0:
        print("Seriously?!")
        return render(request, "tryagain.html")
    
    
    elif request.session["usernum"]  < actualnum:
        print ("Too low!")
        return render(request, "low.html")
    
     
    return render(request, "win.html")
    

def destroy(request):
    print("*"*87)
    del request.session["usernum"]
    return redirect("/")
        
    






