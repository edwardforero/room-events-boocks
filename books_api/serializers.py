from rest_framework import serializers

from custom_auth.serializers import CustomAuthSerializer
from events_api.serializers import EventsSerializer
from custom_auth.models import User
from events_api.models import Events
from books_api.models import Books


class BooksSerializer(serializers.ModelSerializer):
   user = CustomAuthSerializer(read_only=True)
   user_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=User.objects.all(), source='user')
   event = EventsSerializer(read_only=True)
   event_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Events.objects.all(), source='event')
   class Meta:
      model = Books
      fields = "__all__"
   
   def to_internal_value(self, data):
      print(data)
      data['user'] = '<Set Value Here>'
      print("######")
      return super(BooksSerializer, self).to_internal_value(data)
