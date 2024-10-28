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
    full_name = models.CharField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.role = 'Администратор'
        if not self.password.startswith('pbkdf2_'):
            self.set_password(self.password)
        self.full_name = f'{self.firstName} {self.lastName}'
        print(self.full_name)
        return super().save(*args, **kwargs)

    def str(self):
        return self.username
