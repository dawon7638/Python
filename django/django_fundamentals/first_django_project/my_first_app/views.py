from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect



def myblog(request):
    return HttpResponse("hello!")
def new(request):
    return HttpResponse("placeholder")
def goback(request):
    return redirect ("/")
def create(request):
    return HttpResponse("Homepage!")
def show(request, nums):
    return HttpResponse(nums)
def edit(request, nums):
    return HttpResponse(f"placeholder to edit blog {nums}")
def destroy(request, nums):
    return redirect ("/blogs")





    
