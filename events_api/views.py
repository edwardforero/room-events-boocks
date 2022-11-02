
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from events_api.models import Events
from events_api.serializers import EventsSerializer
from custom_auth.permissions import CustomRolePermissions
from custom_auth.utils import get_user_data_using_jwt
from custom_auth.models import User



class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class EventsView(viewsets.ModelViewSet):
   permission_classes = [IsAuthenticated, CustomRolePermissions|ReadOnly]
   queryset = Events.objects.all()
   serializer_class = EventsSerializer
   filters = {}
   user = None

   def get_user_data(self, request):
      self.user = get_user_data_using_jwt(request)

   def add_type_filter(self, request):
      self.get_user_data(request)
      if self.user.role == User.CUSTOMER:
         self.filters["type"] = Events.PUBLIC
      return self.filters

   def list(self, request):
      self.add_type_filter(request)
      queryset = Events.objects.filter(**self.filters)
      serializer = EventsSerializer(queryset, many=True)
      return Response(serializer.data)

   def retrieve(self, request, pk=None):
      self.add_type_filter(request)
      self.filters['id'] = pk 
      queryset = Events.objects.get(**self.filters)
      serializer = EventsSerializer(queryset)
      return Response(serializer.data)
