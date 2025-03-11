from django.shortcuts import render
from .models import Product

def catolog(request):
    products = Product.objects.all()
    return render(request, "shop/catolog.html", {'products': products})