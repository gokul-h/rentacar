from django.shortcuts import render, redirect
from main.models import car
from payment.models import carorder


def home(request):
    return render(request, 'index.html')


def products(request):
    cars = car.objects.all()
    return render(request, 'products.html', {'cars': cars})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def orders(request):
    cars = car.objects.all()
    username = request.user.username
    order = carorder.objects.filter(username=username)
    return render(request, 'orders.html', {'orders': order, 'car': cars})


def checkout(request):
    return render(request, 'checkout.html')
