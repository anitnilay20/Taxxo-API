from __future__ import unicode_literals

from django.db import models
from ledgers.models import Ledgers
from django.utils import timezone


class LedgerHistory(models.Model):
    name = models.ForeignKey(Ledgers, related_name='journalsname')
    type = models.CharField(max_length=1000)
    to_account = models.ManyToManyField(Ledgers, related_name='journalstoaccount')
    date = models.DateTimeField(default=timezone.now)
    closing_balance = models.IntegerField()
    total_amount = models.IntegerField()
