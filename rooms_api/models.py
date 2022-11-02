from django.db import models
from django.core.validators import MinValueValidator, ProhibitNullCharactersValidator


class Rooms(models.Model):
    capacity = models.IntegerField(
                validators=[
                    MinValueValidator(1, message="Capacity must be greater than 1"),
                    ProhibitNullCharactersValidator(message="Capacity can't be null"),
                ]
            )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

