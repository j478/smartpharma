from rest_framework import serializers
from .models import Meds, Accounts
from passlib.hash import pbkdf2_sha256 as sha
from rest_framework.exceptions import PermissionDenied

class MedsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meds
        fields = ("prodName", "amtPerscribed", "amtInStock")

class VerifyLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = ("username", "password")

class CreateAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = ("username", "password")
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        try:
            Accounts.objects.get(username=validated_data['username']) #throws Accounts.DoesNotExist if fails
            raise PermissionDenied('username already exists!') #We dont want to create duplicate accounts, so we error out
        except Accounts.DoesNotExist:
            Account = Accounts.objects.create(
               username = validated_data['username'],
               password = sha.encrypt(validated_data['password'], rounds=12000, salt_size=32) #encrypts password with sha_256
             )

            return Account