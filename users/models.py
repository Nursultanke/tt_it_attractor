from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField('username', max_length=150, unique=True, error_messages={
            'unique': "Пользователь с таким именем уже существует.",
        },)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Все пользователи"
