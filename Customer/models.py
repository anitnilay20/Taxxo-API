from __future__ import unicode_literals
from django.db import models
# Create your models here.
from Taxxo import settings
from django.contrib.auth.models import AbstractUser, PermissionsMixin


class Profile(AbstractUser, PermissionsMixin):
    number = models.IntegerField(blank=True, default=10)
    birth_date = models.DateField(null=True, blank=True)
    is_superuser = models.BooleanField()
