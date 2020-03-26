from django.db import models
from datetime import datetime
from user_management.models import User


class Alumni(models.Model):
    name = models.TextField(null=False)
    email = models.EmailField(null=False)
    phone = models.CharField(max_length=15, null=False, unique=True)
    year_of_passing = models.CharField(max_length=5, null=False)
    date_of_birth = models.DateField(null=False)
    martial_status = models.TextField(null=False)
    profession = models.TextField(null=False)
    address = models.TextField(null=False)
    graduation = models.TextField(null=False)
    graduation1 = models.TextField(null=False)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    last_updated = models.DateTimeField(default=datetime.now, blank=True)
    requestor = models.ForeignKey(User, default=1, null=False, on_delete=models.CASCADE, related_name='alumni_requestor')

    def __str__(self):
        return self.name
