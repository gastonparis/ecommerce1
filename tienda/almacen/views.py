from django.shortcuts import render

def almacen(request):
    context = {}
    return render(request, 'almacen/almacen.html', context)

def carrito(request):
    context = {}
    return render(request, 'almacen/carrito.html', context)

def checkout(request):
    context = {}
    return render(request, 'almacen/checkout.html', context)