from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.db import models


from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    dni = models.CharField('DNI', primary_key=True, unique=True, max_length=8)
    nombres = models.CharField('Nombres', max_length=100, null=False)
    apellidos = models.CharField('Apellidos', max_length=100, null=False)
    email = models.EmailField('email', unique=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'dni'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.dni

