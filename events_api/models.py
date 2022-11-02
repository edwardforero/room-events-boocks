from django.db import models

from rooms_api.models import Rooms


class Events(models.Model):

    PRIVATE = 'PR'
    PUBLIC = 'PU'
    EVENT_TYPES = [
        (PRIVATE, 'Private'),
        (PUBLIC, 'Public'),
    ]
    date = models.DateField()
    room = models.ForeignKey(Rooms, on_delete=models.RESTRICT)
    type = models.CharField(
        max_length=2,
        choices=EVENT_TYPES,
        error_messages={"invalid_choice": "Please select: PR for Private and PU for Public"}
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [
            ("date", "room"),
        ]
