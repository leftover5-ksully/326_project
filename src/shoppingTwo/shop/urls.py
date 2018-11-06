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

urlpatterns += [
    path("stores/", views.StoreListView.as_view(), name="stores"),
    path("item_cart/<int:pk>", views.StoreDetailView.as_view(), name="items_cart")
]
