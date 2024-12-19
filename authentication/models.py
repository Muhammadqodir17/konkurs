from django.contrib.auth.models import AbstractUser
from django.db import models
from .validators import validate_uz_phone_number


class User(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    third_name = models.CharField(max_length=30)
    email = models.EmailField()
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=13, validators=[validate_uz_phone_number])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
