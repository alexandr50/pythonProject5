from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    first_name = None
    last_name = None
    email = None
    username = None

    phone_number = PhoneNumberField(max_length=20, verbose_name='phone_number', unique=True)

    objects = UserManager()

    def __str__(self):
        return str(self.phone_number)



