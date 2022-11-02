
from rest_framework import status
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rooms_api.models import Rooms
from rooms_api.serializers import RoomsSerializer
from custom_auth.permissions import CustomRolePermissions



class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class RoomsView(viewsets.ModelViewSet):
   permission_classes = [IsAuthenticated, CustomRolePermissions|ReadOnly]
   queryset = Rooms.objects.all()
   serializer_class = RoomsSerializer
