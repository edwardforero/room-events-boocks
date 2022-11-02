from rest_framework import permissions

from rest_framework_simplejwt.authentication import JWTAuthentication

from custom_auth.models import User


class CustomRolePermissions(permissions.BasePermission):

    def has_permission(self, request, view):
      JWT_authenticator = JWTAuthentication()
      response = JWT_authenticator.authenticate(request)
      user, _ = response
      role = User.objects.values_list('role', flat=True).get(email=user)
      return role == User.BUSINESS

    def has_object_permission(self, request, view, obj):
        return True