from django.shortcuts import render

def store(request):
    contex = {}
    return render(request, 'store.html', contex)

def cart(request):
    contex = {}
    return render(request, 'cart.html', contex)

def checkout(request):
    contex = {}
    return render(request, 'checkout.html', contex)


