from django.core import serializers
from rest_framework import status
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from events_api.models import Events
from books_api.models import Books
from books_api.serializers import BooksSerializer
from custom_auth.utils import get_user_data_using_jwt
from custom_auth.models import User



class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class BooksView(viewsets.ModelViewSet):
   
   permission_classes = [IsAuthenticated]
   queryset = Events.objects.all()
   serializer_class = BooksSerializer
   filters = {}
   user = None


   def get_user_data(self, request):
      self.user = get_user_data_using_jwt(request)


   def add_user_filter(self, request):
      self.get_user_data(request)
      if self.user.role != User.BUSINESS:
         self.filters["user_id"] = self.user.id
      return self.filters

   def list(self, request):
      filters = self.add_user_filter(request)
      queryset = Books.objects.filter(**filters)
      serializer = BooksSerializer(queryset, many=True)
      return Response(serializer.data)

   
   def retrieve(self, request, pk=None):
      filters = self.add_user_filter(request)
      filters['id'] = pk
      queryset = Books.objects.get(**filters)
      serializer = BooksSerializer(queryset)
      return Response(serializer.data)

   def create(self, request):
      self.get_user_data(request)
      request.data["user_id"] = self.user.id
      serializer = self.get_serializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      event_data = serializer.validated_data["event"]
      room_data = event_data.room
      if event_data.type == Events.PRIVATE:
         return Response({"error": "This event is private"}, status=status.HTTP_403_FORBIDDEN,)
      total_books = Books.objects.filter(event_id=event_data.id).count()
      if total_books >= room_data.capacity:
         return Response({"error": "Event without capacuty."}, status=status.HTTP_403_FORBIDDEN,)

      self.perform_create(serializer)
      headers = self.get_success_headers(serializer.data)
      return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

   def destroy(self, request, pk=None):
      self.get_user_data(request)
      book_data = Books.objects.filter(pk=pk)
      if len(book_data) == 0:
         return Response({"error": "Book not found."}, status=status.HTTP_404_NOT_FOUND)
      book_data = book_data[0]
      if book_data.user.id != self.user.id:
         return Response({"error": "This book doesn't belong to you."}, status=status.HTTP_403_FORBIDDEN)
      book_data.delete()
      return Response({"msg": "Book %s deleted." % pk}, status=status.HTTP_201_CREATED)


   def update(self, request, pk=None):
      return Response({"error": "Event can't be modified."}, status=status.HTTP_403_FORBIDDEN)

   def partial_update(self, request, pk=None):
      return Response({"error": "Event can't be modified."}, status=status.HTTP_403_FORBIDDEN)
   