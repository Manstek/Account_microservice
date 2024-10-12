from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    first_name = None
    last_name = None

    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    role = models.CharField(
        max_length=50, choices=settings.ROLES, default='user')

    def str(self):
        return self.username
