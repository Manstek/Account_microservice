from django.db import models
from django.contrib.auth.models import AbstractUser
ROLES = [
    ('doctor', 'Доктор'),
    ('user', 'Пользователь'),
    ('admin', 'Администратор'),
]


class User(AbstractUser):
    roles = models.CharField(max_length=50, choices=ROLES, default='user')

    def str(self):
        return self.username
