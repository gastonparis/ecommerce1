from django.urls import path
from . import views

urlpatterns = [
    path('', views.almacen, name="almacen"),
    path('carrito/', views.carrito, name="carrito"),
    path('checkout/', views.checkout, name="checkout"),
]