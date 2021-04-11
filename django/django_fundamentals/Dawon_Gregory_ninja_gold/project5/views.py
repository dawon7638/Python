from django.shortcuts import render, redirect
import random 


# Create your views here.




def index(request):
    farm = random.randint(10, 20)
    print("*"*87)
    print(request.GET)
    if not "counter" in request.session:
        request.session["counter"] = 0
    if not "activities" in request.session:
        request.session["activities"] =[]
        print("counter does not exist")
    print(request.session["counter"])    
    return render(request, "page1.html")


def getmoney(request):
    activities = []
    mulah = random.randint(2, 5)
    mulac = random.randint(5, 10)
    mulaf = random.randint(10, 20)
    mulacs = random.randint(-50, 50)
    if request.GET["getgold"] == "farm":
        request.session["counter"] += mulaf
        request.session["activities"].append(f" Earned {mulaf} golds from the farm!")
        print("*"*87)
        
        
    
    elif request.GET["getgold"] == "cave":
        request.session["counter"] += mulac
        request.session["activities"].append(f" Earned {mulac} golds from the cave!")
        
        
    elif request.GET["getgold"] == "house":
        request.session["counter"] += mulah
        request.session["activities"].append(f" Earned {mulah} golds from the house!")
        
        
    elif request.GET["getgold"] == "casino":
        request.session["counter"] += mulacs
        
        if mulacs < 0:
            request.session["activities"].append(f" Entered a casino and lost {mulacs} golds.. Ouch.")
        
        elif mulacs == 0:
            request.session["activities"].append(f" Entered a casino and lost ALL golds!")
            del request.session["counter"]
            del request.session["activities"]
            return redirect(request,"page2.html" )
        
        else:
            request.session["activities"].append(f" Entered a casino and won {mulacs} golds.  Luck is on your side!")
    return redirect("/")

def destroy(request):
    print("*"*87)
    del request.session["counter"]
    return redirect("/")
