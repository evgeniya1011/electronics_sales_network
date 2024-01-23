from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    phone_number = models.CharField(max_length=50,
                                    verbose_name='Номер телефона',
                                    **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
