from rest_framework import serializers

from custom_auth.models import User

class CustomAuthSerializer(serializers.ModelSerializer):
   class Meta:
      model = User
      fields = ("id", "email", "password", "is_superuser", "role", "created_at", "updated_at", )
      extra_kwargs = {"role": {"error_messages": {"invalid_choice": "Please select: BU for Bussines and CU for Customer"}}}

