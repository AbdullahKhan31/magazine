from django.db import models
from datetime import datetime
from user_management.models import User

class AuditoriumReservation(models.Model):
    reason = models.TextField(null=False)
    start_time = models.DateTimeField(null=False)
    end_time = models.DateTimeField(null=False)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    last_updated = models.DateTimeField(default=datetime.now, blank=True)
    requestor = models.ForeignKey(User, default=1, null=False, on_delete=models.CASCADE, related_name='auditoriumreservation_requestor')

    def __str__(self):
        return self.Reason

