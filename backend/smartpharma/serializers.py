from rest_framework import serializers
from .models import Smartpharma

class SmartpharmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Smartpharma
        fields = ("prodName", "prodNum", "prodColor")