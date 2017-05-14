from __future__ import unicode_literals
from django.db import models
from journal.models import Journal
from Customer.models import Profile
from django.utils import timezone


class Sales(models.Model):
    party_name = models.CharField(max_length=1000)
    date = models.DateField(default=timezone.now)
    journals = models.ManyToManyField(Journal,related_name='juurnal')
    payment_method = models.CharField(max_length=1000)
    total_amount = models.IntegerField()
    added_by = models.ForeignKey(Profile)