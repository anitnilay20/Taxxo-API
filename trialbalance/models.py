from __future__ import unicode_literals
from django.db import models
from ledgers.models import Ledgers
from company.models import Company


class TrialBalance(models.Model):
    particular = models.CharField(max_length=1000)
    debitAmount = models.IntegerField()
    creditAmount = models.IntegerField()
    ledger = models.ForeignKey(Ledgers)
    company = models.ForeignKey(Company)
