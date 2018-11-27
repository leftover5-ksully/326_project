from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    path("", views.homepage.as_view(), name="homepage")
]

urlpatterns += [
    path('homepage/', views.homepage.as_view(), name="homepage"),
]

urlpatterns += [
    path('store_items/', views.store_items, name="store_items"),
]

urlpatterns += [
    path('addItem/', views.addItem, name="addItem"),
]

urlpatterns += [
    path('addItem/success/', views.addItem_success , name="addItem_success"),
]

urlpatterns += [
    path('profile/', views.profile, name="profile"),
]

urlpatterns += [
    path('profile/favoriteCart', views.favorite_cart, name="favorite_cart"),
]

urlpatterns += [
    path("stores/", views.StoreListView.as_view(), name="stores"),
    path("item_cart/<int:pk>", views.StoreDetailView.as_view(), name="items_cart"),
    path('profile/favoriteItems', views.favorite_items, name="favorite_items"),
    path('profile/favoriteItems2', views.favorite_items2, name="favorite_items2"),
    path('profile/user_preferences', views.user_preferences, name="user_preferences")
]

urlpatterns += [
    path('map/', views.map.as_view(), name="map"),
]

urlpatterns += [
    path('signin/', views.signin, name="signin"),
]

urlpatterns += [
    path('login_error/', views.login_error, name="login_error"),
]

urlpatterns += [path("admin/", admin.site.urls)]
