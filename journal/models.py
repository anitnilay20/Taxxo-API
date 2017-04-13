from __future__ import unicode_literals
from django.db import models


class Journal(models.Model):
    credit_amount = models.IntegerField()
    debit_amount = models.IntegerField()
    narration = models.CharField(max_length=1000)
    credit_account = models.CharField(max_length=1000)
    debit_account = models.CharField(max_length=1000)
