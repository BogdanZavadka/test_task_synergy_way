"""This module contains view methods that return html templates for a frontend"""
from django.shortcuts import render
from test_task_app.models import User, Address, CreditCard

def user_list(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})

def address_list(request):
    addresses = Address.objects.all()
    return render(request, 'addresses.html', {'addresses': addresses})

def credit_card_list(request):
    cards = CreditCard.objects.all()
    return render(request, 'credit_cards.html', {'cards': cards})

def home(request):
    return render(request, 'home.html')

