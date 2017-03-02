from __future__ import unicode_literals

from django.db import models
from company.models import Company
from ledgers.models import Ledgers
from Customer.models import Profile
from django.utils import timezone

class Receipt(models.Model):
    company = models.ForeignKey(Company)
    firstAccount = models.ForeignKey(Ledgers, related_name="receiptFirstAccount")
    secondAccount = models.ForeignKey(Ledgers, related_name="receiptSecondAccount")
    amount = models.IntegerField()
    addedBy = models.ForeignKey(Profile)
    date = models.DateTimeField(default=timezone.now)
    narration = models.TextField(max_length=100000, blank=True)