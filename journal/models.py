from __future__ import unicode_literals
from django.db import models
from ledgers.models import Ledgers
from company.models import Company
from django.utils import timezone


class Journal(models.Model):
    company = models.ForeignKey(Company)
    credit_amount = models.IntegerField()
    debit_amount = models.IntegerField()
    narration = models.CharField(max_length=1000, blank=True)
    for_account = models.ForeignKey(Ledgers,related_name="journalforaccount")
    to_Account = models.ManyToManyField(Ledgers,related_name="journaltoaccount")
    date = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if self.credit_amount > self.debit_amount:
            self.for_account.credit_amount += self.credit_amount
        else:
            self.for_account.debit_amount += self.debit_amount
        self.for_account.save()
        super(Journal, self).save()
  
