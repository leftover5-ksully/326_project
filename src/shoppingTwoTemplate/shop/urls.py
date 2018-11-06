from django.urls import path
from . import views

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
    path('profile/', views.profile, name="profile"),
]

urlpatterns += [
    path('profile/favoriteCart', views.favorite_cart, name="favorite_cart"),
]

urlpatterns += [
    path('profile/favoriteItems', views.favorite_items, name="favorite_items"),
]

urlpatterns += [
    path('map/', views.map.as_view(), name="map"),
]

urlpatterns += [
    path('signin/', views.signin, name="signin"),
]