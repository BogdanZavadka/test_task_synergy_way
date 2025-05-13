"""This module contains url patterns of a frontend app"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('view_users/', views.user_list, name='user_list'),
    path('view_addresses/', views.address_list, name='address_list'),
    path('view_cards/', views.credit_card_list, name='credit_card_list'),
]
