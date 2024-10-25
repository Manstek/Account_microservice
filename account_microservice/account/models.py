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

    @property
    def full_name(self):
        return f'{self.lastName} {self.firstName}'

    def save(self, *args, **kwargs):
        print(self.full_name)
        if self.is_superuser:
            self.role = 'Администратор'
        if not self.password.startswith('pbkdf2_'):
            self.set_password(self.password)
        return super().save(*args, **kwargs)

    def str(self):
        return self.username
