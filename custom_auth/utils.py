from rest_framework_simplejwt.authentication import JWTAuthentication
from django.core import serializers
from custom_auth.models import User


def get_user_data_using_jwt(request):
    JWT_authenticator = JWTAuthentication()
    response = JWT_authenticator.authenticate(request)
    user, _ = response
    return user