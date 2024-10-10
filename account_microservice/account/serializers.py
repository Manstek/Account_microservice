from rest_framework import serializers
from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer
from .models import User

# User = get_user_model()


class CustomUserCreateSerializer(UserCreateSerializer):
    firstName = serializers.CharField(required=True)
    lastName = serializers.CharField(required=True)

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'lastName', 'firstName', 'username', 'password')
