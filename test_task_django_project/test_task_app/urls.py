"""This module contains url patterns of a backend app"""
from django.urls import path
from .views import (get_users, create_user, get_addresses, create_address,
                    get_credit_cards, create_credit_card)

urlpatterns = [
    path('users/', get_users, name='get_users'),
    path('users/create', create_user, name='create_user'),
    path('addresses/', get_addresses, name='get_addresses'),
    path('addresses/create', create_address, name='create_address'),
    path('credit_cards/', get_credit_cards, name='get_credit_cards'),
    path('credit_cards/create', create_credit_card, name='create_credit_card'),
]
