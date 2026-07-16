from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    phone_nomber = models.CharField(max_length=14)

    def __str__(self):
        return f"{self.phone_nomber}"