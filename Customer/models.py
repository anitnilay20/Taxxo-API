from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models


def user_directory_path(instance, filename):
    return 'email_{0}/{1}'.format(instance.email, filename)


class Profile(AbstractUser, PermissionsMixin):
    number = models.IntegerField(blank=True, default=10)
    birth_date = models.DateField(null=True, blank=True)
    is_superuser = models.BooleanField()
    image = models.ImageField(upload_to=user_directory_path, blank=True)
