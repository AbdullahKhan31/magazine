from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    address = models.TextField(null=True)


class Role(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    last_updated = models.DateTimeField(default=datetime.now, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userrole_user')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='userrole_role')
    approver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='userrole_approver')
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    last_updated = models.DateTimeField(default=datetime.now, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.user.name + '__' + self.role.title
