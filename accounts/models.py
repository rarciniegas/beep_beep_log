from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class CustomUser(AbstractUser):
    phone_number = PhoneNumberField(region='US', null=True, blank=True, unique=True)
