from django.shortcuts import render

# Create your views here.

def home_view(request):
    username_is = request.user
    context = {"username": username_is}

    template = 'products/home.html'
    return render(request, template, context)