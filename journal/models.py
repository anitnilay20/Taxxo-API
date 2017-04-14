from __future__ import unicode_literals
from django.db import models
from ledgers.models import Ledgers


class Journal(models.Model):
    credit_amount = models.IntegerField()
    debit_amount = models.IntegerField()
    narration = models.CharField(max_length=1000)
    for_account = models.ForeignKey(Ledgers,related_name="journalforaccount")
    to_Account = models.ForeignKey(Ledgers,related_name="journaltoaccount")
    date = models.DateField()
