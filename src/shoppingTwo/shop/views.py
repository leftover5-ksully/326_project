from django.shortcuts import render
# Create your views here.

def homepage(request):
    return render(request, "homepage.html")

def cartOne(request):
    return render(request, "homepage.html")

def cartTwo(request):
    return render(request, "homepage.html")

def cartThree(request):
    return render(request, "homepage.html")

def map(request):
    return render(request, "homepage.html")