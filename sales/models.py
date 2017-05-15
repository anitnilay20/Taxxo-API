from __future__ import unicode_literals
from django.db import models
from journal.models import Journal
from Customer.models import Profile
from django.utils import timezone
from company.models import Company
from ledgers.models import Ledgers


class Sales(models.Model):
    party_name = models.ForeignKey(Ledgers)
    date = models.DateField(default=timezone.now)
    journals = models.ManyToManyField(Journal, related_name='Sales_journal')
    payment_method = models.CharField(max_length=1000)
    total_amount = models.IntegerField()
    narration = models.CharField(max_length=1000)
    company = models.ForeignKey(Company)
    added_by = models.ForeignKey(Profile)
