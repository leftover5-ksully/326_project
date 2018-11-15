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
    #user = UserModel.objects.filter(username__exact="defaultUser")
    #context = {"user": user}
    return render(request, "profilePage.html")

class map(generic.ListView):
    model = Store
    template_name = "map.html"

def signin(request):
    return render(request, "signin.html")

def favorite_cart(request):
    if request.user.is_authenticated:
        userM = UserModel.objects.filter(user__exact=request.user)
        user = request.user
        context = {"userM": userM,
                   "user": user}
        return render(request, "favorite_cart.html", context=context)
    return render(request, "login_error.html")

class StoreListView(generic.ListView):
    model = Store
    template_name = "store_list.html"

class StoreDetailView(generic.DetailView):
    model = Store
    template_name = "items_cart.html"

def favorite_items(request):
    if request.user.is_authenticated:
        userM = UserModel.objects.filter(user__exact=request.user)
        user = request.user
        context = {"userM": userM,
                   "user": user}
        return render(request, "favorite_items.html", context=context)
    return render(request, "login_error.html")
    
def favorite_items2(request):
    if request.user.is_authenticated:
        userM = UserModel.objects.filter(user__exact=request.user)
        user = request.user
        context = {"userM": userM,
                   "user": user}
        return render(request, "Stats2.html", context=context)
    return render(request, "login_error.html")

def user_preferences(request):
    if request.user.is_authenticated:
        userM = UserModel.objects.filter(user__exact=request.user)
        user = request.user
        context = {"userM": userM,
                   "user": user}
        return render(request, "user_preferences.html", context=context)
    return render(request, "login_error.html")

def login_error(request):
    return render(request, "login_error.html")