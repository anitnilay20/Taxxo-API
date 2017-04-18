from __future__ import unicode_literals
from django.db import models
from journal.models import Journal


class Sales(models.Model):
    Invoice = models.IntegerField()
    party_name = models.CharField(max_length=1000)
    reference = models.IntegerField()
    journals = models.ManyToManyField(Journal,related_name='juurnal')
    payment_method = models.CharField(max_length=1000)