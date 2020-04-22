from django.shortcuts import render
from .models import Product

# Create your views here.

def home_view(request):
    products = Product.objects.all()
    username = request.user
    context = {
        'products': products,
        'username': username,
    }

    template = 'products/home.html'
    return render(request, template, context)

def all_view(request):
    products = Product.objects.all()
    context = {'products': products}
    
    template = 'products/all.html'
    return render(request, template, context)