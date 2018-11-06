from django.shortcuts import render

from shop.models import Item, List, UserModel, Store
from django.views import generic

# Create your views here.

class homepage(generic.ListView):
    model = Store
    template_name = "homepage.html"

def store_items(request):
    store = Store.objects.filter(storename__exact="defaultStore")
    context = {"store" : store}
    return render(request, "store_items.html", context=context)

def profile(request):
    user = UserModel.objects.filter(username__exact="defaultUser")
    context = {"user": user}
    return render(request, "profilePage.html", context=context)

class map(generic.ListView):
    model = Store
    template_name = "map.html"

def signin(request):
    return render(request, "signin.html")

def favorite_cart(request):
    user = UserModel.objects.filter(username__exact="defaultUser")
    context = {"user": user}
    return render(request, "favorite_cart.html", context=context)


class StoreListView(generic.ListView):
    model = Store
    template_name = "store_list.html"

class StoreDetailView(generic.DetailView):
    model = Store
    template_name = "items_cart.html"

def favorite_items(request):
    user = UserModel.objects.filter(username__exact="defaultUser")
    context = {"user": user}
    return render(request, "favorite_items.html", context=context)
    
def favorite_items2(request):
    user = UserModel.objects.filter(username__exact="defaultUser")
    context = {"user": user}
    return render(request, "Stats2.html", context=context)

def user_preferences(request):
    user = UserModel.objects.filter(username__exact="defaultUser")
    context = {"user": user}
    return render(request, "user_preferences.html", context=context)