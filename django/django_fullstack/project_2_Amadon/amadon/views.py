from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "index.html", context)

def checkoutForm(request):
    quantity_from_form = int(request.POST["quantity"])
    price_from_form = float(request.POST["id"])
    print(request.POST)
    total_charge = quantity_from_form * price_from_form
    print("Charging credit card...")
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    return redirect("/")


def checkoutThx(request, num):
    print("*"*87)
    product = Product.objects.all()
    print(product)
    print("*"*87)
    
    
    print("*"*87)
    order = Order.objects.all()
    print(order)
    print("*"*87)
    
    
    context = {
        "all_products" : product,
        
        "all_orders": order,
    }
    
    return render(request, "checkout.html", context)