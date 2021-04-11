from django.shortcuts import render, HttpResponse, redirect



    # if "count".request.session:
    # else: request.session.counter = 1:



def index(request):
    print("*"*87)
    if not "counter" in request.session:
        request.session["counter"] = 0
        print("counter does not exist")
    request.session["counter"] += 1    
    print(request.session["counter"])
    return render(request, "index.html")f


def destroy(request):
    print("*"*87)
    del request.session["counter"]
    return redirect('/')




