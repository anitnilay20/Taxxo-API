from __future__ import unicode_literals
from django.db import models
from journal.models import Journal
from Customer.models import Profile


class Purchase(models.Model):
    Invoice = models.IntegerField()
    party_name = models.CharField(max_length=1000)
    reference = models.IntegerField()
    journals = models.ManyToManyField(Journal,related_name='Journaljournals')
    payment_method = models.CharField(max_length=1000)
    added_by = models.ForeignKey(Profile)
