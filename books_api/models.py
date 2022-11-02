from django.db import models

from custom_auth.models import User
from events_api.models import Events


class Books(models.Model):

    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    event = models.ForeignKey(Events, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [
            ("user", "event"),
        ]

