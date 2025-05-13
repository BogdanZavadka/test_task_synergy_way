"""This module includes the models that represent the tables from a database"""
from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

class Address(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    country = models.CharField(max_length=20)
    region = models.CharField(max_length=25, null=True)
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=50)
    house_number = models.IntegerField()
    postal_code = models.CharField(max_length=20, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class CreditCard(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    card_number = models.CharField(max_length=20)
    cvv = models.IntegerField()
    expiration_date = models.DateTimeField()
    bank_name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
