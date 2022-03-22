from rest_framework import serializers
from .models import Meds, Accounts

class MedsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meds
        fields = ("prodName", "amtPerscribed", "amtInStock")

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = ("username", "password")