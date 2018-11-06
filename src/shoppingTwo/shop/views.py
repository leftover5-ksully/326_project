from django.shortcuts import render
from shop.models import Store, Item
from django.views import generic
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

class StoreListView(generic.ListView):
    model = Store
    template_name = "store_list.html"

class StoreDetailView(generic.DetailView):
    model = Store
    template_name = "items_cart.html"
