from __future__ import unicode_literals
from django.db import models
from ledgers.models import 


class Journal(models.Model):
    credit_amount = models.IntegerField()
    debit_amount = models.IntegerField()
    narration = models.CharField(max_length=1000)
    foraccount = models.ForeignKey(Ledgers)
    toAccount = models.ForeignKey(Ledgers)
    date = models.DateField()
