"""This module contains serializer classes used in views"""
from rest_framework.serializers import ModelSerializer
from .models import User, Address, CreditCard


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"

class CreditCardSerializer(ModelSerializer):
    class Meta:
        model = CreditCard
        fields = "__all__"
