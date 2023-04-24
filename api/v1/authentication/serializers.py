from typing import Any, Dict
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.serializers import TokenObtainSerializer, TokenObtainPairSerializer
from rest_framework import exceptions
from .models import UserProfile, User
from django.utils import timezone

class CustomTokenObtainSerializer(TokenObtainSerializer):

    profile = None
    default_error_messages = {
        **TokenObtainPairSerializer.default_error_messages,
        'failed_attempts' : 'Has ingresado credenciales incorrectas 3 veces. Tu cuenta ha sido bloqueada por 5 minutos.',
    }
    
    

    def lock_account(self):
        self.profile.lock_account(5)
        raise exceptions.AuthenticationFailed(
            self.error_messages['failed_attempts'],
                'failed_attempts'
        )


    def verify_attempts(self,attrs):
        current_user = User.objects.filter(email=attrs.get(self.username_field)).first()
        if not current_user: return

        # Si las credenciales son incorrectas, incrementamos el contador de intentos fallidos
        self.profile,_ = UserProfile.objects.get_or_create(user=current_user)
        self.profile.increment_failed_attempts()
        
        if self.profile.failed_attempts >= 3: self.lock_account()

    def verify_account_blocking(self):
        self.profile,_ = UserProfile.objects.get_or_create(user=self.user)
        
        if self.profile.is_account_locked():
            remaining_time = (self.profile.locked_until - timezone.now()).seconds // 60
            self.error_messages['account_locked'] = f'Tu cuenta está bloqueada, vuelve a intentarlo dentro de {remaining_time} minutos.'
            raise exceptions.AuthenticationFailed(
                self.error_messages['account_locked'],
                'account_locked'
            )
        
        self.profile.reset_failed_attempts() 

    def validate(self, attrs: Dict[str, Any]) -> Dict[Any, Any]:
        authenticate_kwargs = {
            self.username_field: attrs[self.username_field],
            "password": attrs["password"],
        }
        try:
            authenticate_kwargs["request"] = self.context["request"]
        except KeyError:
            pass

        self.user = authenticate(**authenticate_kwargs)

        if not api_settings.USER_AUTHENTICATION_RULE(self.user):
            # Attempts logic
            self.verify_attempts(attrs)

            raise exceptions.AuthenticationFailed(
                self.error_messages["no_active_account"],
                "no_active_account",
            )
        # Successful login

        self.verify_account_blocking()

        return {}



class CustomTokenObtainPairSerializer(TokenObtainPairSerializer,CustomTokenObtainSerializer):pass