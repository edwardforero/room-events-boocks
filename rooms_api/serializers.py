from rest_framework import serializers

from rooms_api.models import Rooms


class RoomsSerializer(serializers.ModelSerializer):
   class Meta:
      model = Rooms
      fields = ("id", "capacity", )

