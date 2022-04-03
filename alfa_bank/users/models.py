from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_support = models.BooleanField(default=False, verbose_name="It's support")
    address = models.TextField(blank=True,max_length=100, verbose_name="client address")
    photo = models.ImageField(blank=True, upload_to="photos/%Y/%m/%d/", verbose_name="Photo")
    email = models.EmailField(max_length=100, unique=True)

    def __str__(self):
        return self.username
