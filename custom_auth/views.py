from rest_framework import viewsets

from custom_auth.models import User
from custom_auth.serializers import CustomAuthSerializer
from rest_framework.permissions import IsAuthenticated
from custom_auth.permissions import CustomAdminPermissions



class CustomUserView(viewsets.ModelViewSet):
   permission_classes = [IsAuthenticated, CustomAdminPermissions]
   queryset = User.objects.all()
   serializer_class = CustomAuthSerializer
