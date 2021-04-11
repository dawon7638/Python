from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from semi_restful_tv_shows.models import Show

####################################################################






def create(request):#Landing page for creatForm
    return render(request, "create.html")

def createForm(request):
    print("************************FORM DATA************************")
    print(request.POST)
    print("************************FORM DATA************************")
    Show.objects.create(title = request.POST["title"], 
                        network = request.POST["network"], 
                        release_date = request.POST["release_date"], 
                        desc = request.POST["desc"])
    return redirect("/shows")
  
####################################################################
def read_all(request):#Landing page for read_all
    print("************************ALL SHOWS PAGE************************")
    print(request.POST)
    print("************************ALL SHOWS PAGE************************")
    show = Show.objects.all()
    context = {
        "all_tvShows": show,
    }
    return render (request, "read_all.html", context)

def read_one(request, num):#Landing page for read_one
    print("************************SHOW DESCRIPTIONS************************")
    print(request.POST)
    print("************************SHOW DESCRIPTIONS************************")
    tv_shows = Show.objects.filter(id=num)
    context = {
        "current_show": tv_shows
    }
    return render(request,"read_one.html", context)

####################################################################
def update(request, num):#UpdateForm landing page
    tv_shows = Show.objects.filter(id=num)
    context = {
        "current_show": tv_shows
    }
    return render(request, "update.html", context)

def updateForm(request):
    print("************************UPDATEFORM DATA************************")
    print(request.POST)
    print("************************UPDATEFORM DATA************************")
    Show.objects.update(title = request.POST["title"], 
                        network = request.POST["network"], 
                        release_date = request.POST["release_date"], 
                        desc = request.POST["desc"])
    return redirect("/shows/<int:num>")
####################################################################

# def destroy(request, num):#Destroy single record
#     show = Show.ogjects.filter(id=num)
#     if num = current.id:
        
    
#     show_to_delete = Show.objects.get(id=num)	# let's retrieve a single movie,
#     show_to_delete.delete()	# and then delete it
#     return redirect("/shows")







