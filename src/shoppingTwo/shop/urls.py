from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage")
]

urlpatterns += [
    path('cart1/', views.cartOne, name="cartOne"),
]

urlpatterns += [
    path('cart2/', views.cartTwo, name="cartTwo"),
]

urlpatterns += [
    path('cart3/', views.cartThree, name="cartThree"),
]

urlpatterns += [
    path('map/', views.map, name="map"),
]
