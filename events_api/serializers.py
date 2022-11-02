from rest_framework import serializers

from rooms_api.serializers import RoomsSerializer
from rooms_api.models import Rooms
from events_api.models import Events


class EventsSerializer(serializers.ModelSerializer):
   room = RoomsSerializer(read_only=True)
   room_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Rooms.objects.all(), source='room')
   class Meta:
      model = Events
      #   fields = ("id", "date", "room", "type")
      fields = "__all__"
      extra_kwargs = {"type": {"error_messages": {"invalid_choice": "Please select: PR for Private and PU for Public"}}}

