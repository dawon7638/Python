from django.shortcuts import render, HttpResponse











def index(request):
     print("*"*87)
     
     return render(request, "index.html")


def nextpage(request):
     print("*"*87)
     print(request.POST)
     print("Processing form...")
     
     context = {
          "user_name": request.POST["user_name"], "location": request.POST["location"], "language": request.POST["language"], "comment": request.POST["comment"]
     }
     
   
     return render(request, "index2.html", context)



