from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from Customer.models import Profile


class Activity(models.Model):
    name = models.CharField(max_length=1000)
    date = models.DateTimeField(default=timezone.now)
    added_by = models.ForeignKey(Profile)
    amount = models.IntegerField()
