from typing import Any, Dict
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.serializers import TokenObtainSerializer, TokenObtainPairSerializer
from rest_framework import exceptions
from .models import User
from django.utils import timezone

class CustomTokenObtainSerializer(TokenObtainSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        # Agrega más datos personalizados a la respuesta
        data['username'] = self.user.username
        data['company'] = self.user.first_name
        data['role_id'] = self.user.user_role.id
        data['role_description'] = self.user.user_role.description

        return data


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer,CustomTokenObtainSerializer):pass

from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'