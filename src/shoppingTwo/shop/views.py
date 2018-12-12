from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import permission_required
from shop.models import Item, List, UserModel, Store
from shop.forms import AddItemForm
from django.views import generic
from faker import Faker
from django.contrib.auth.forms import PasswordChangeForm


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
                   
                   
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Important!
                messages.success(request, 'Your password was successfully updated!')
                return redirect('user_preferences')
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            #form = PasswordChangeForm(request.user)
            form = PasswordChangeForm(user)
        return render(request, 'user_preferences.html', {
            'form': form
        })    
        
        #return render(request, "user_preferences.html", context=context)
    return render(request, "login_error.html")

def login_error(request):
    return render(request, "login_error.html")

@permission_required('shop.can_add_items')
def addItem(request):
    fake = Faker()
    if request.user.is_authenticated:
        userM = UserModel.objects.filter(user__exact=request.user)
        user = request.user
        context = {"userM": userM,
                   "user": user}
        if request.method == 'POST':
            form = AddItemForm(request.POST)
            if form.is_valid():
                fakeStore = Store(name=fake.text(50), location=fake.text(10))
                fakeStore.save()
                i_name = form.cleaned_data['new_item']
                i_store = fakeStore
                i_price = fake.random_int(1, 100)
                i_aisle = fake.random_int(1, 26)
                i_short_description = fake.text(150)
                i_item_number = fake.random_int(1, 126)
                item = Item(name=i_name,
                            store=i_store,
                            price=i_price,
                            aisle=i_aisle,
                            short_description=i_short_description,
                            item_number=i_item_number,
                            )
                item.save()
                userM[0].favoriteItems.add(item)
                userM[0].save()
                return HttpResponseRedirect('success/')
        else:
            fakeStore = Store(name=fake.text(50), location=fake.text(10))
            fakeStore.save()
            i_name = fake.text(50)
            i_store = fakeStore
            i_price = fake.random_int(1, 100)
            i_aisle = fake.random_int(1, 26)
            i_short_description = fake.text(150)
            i_item_number = fake.random_int(1, 126)
            def_item = Item(name=i_name,
                        store=i_store,
                        price=i_price,
                        aisle=i_aisle,
                        short_description=i_short_description,
                        item_number=i_item_number,
                        )

            form = AddItemForm(initial={'new_item': def_item,})
        return render(request, "addItem.html", {'form': form})
    return render(request, "login_error.html")

def addItem_success(request):
    return render(request, "success.html")