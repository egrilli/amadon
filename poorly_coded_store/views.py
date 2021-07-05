from django.shortcuts import render,redirect
from .models import Order, Product

def index(request):

    if "cantidad" in request.session:
        del request.session['cantidad']
    
    if "precio" in request.session:
        del request.session['precio']
    
    if "final" in request.session:
        del request.session['final']

    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    quantity_from_form = int(request.POST["quantity"])
    price_from_form = float(request.POST["price"])
    total_charge = quantity_from_form * price_from_form
    
    request.session['cantidad']=quantity_from_form
    request.session['precio']=price_from_form
    request.session['final']=total_charge

    hola=request.session['final']

    print("Charging credit card...")
    print(hola)
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)


    return redirect("/rcheckout/")

def rcheckout(request):
        
    return render(request,"store/checkout.html")
