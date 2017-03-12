from __future__ import unicode_literals

from django.db import models
from company.models import Company
from ledgers.models import Ledgers
from Customer.models import Profile
from django.utils import timezone
from activity.models import Activity

class Receipt(models.Model):
    company = models.ForeignKey(Company)
    firstAccount = models.ForeignKey(Ledgers, related_name="receiptFirstAccount")
    secondAccount = models.ForeignKey(Ledgers, related_name="receiptSecondAccount")
    amount = models.IntegerField()
    addedBy = models.ForeignKey(Profile)
    date = models.DateTimeField(default=timezone.now)
    narration = models.TextField(max_length=100000, blank=True)

    def save(self, *args, **kwrgs):
        self.firstAccount.opening_balance -= self.amount
        self.firstAccount.save(force_update=True)
        self.secondAccount.opening_balance += self.amount
        self.secondAccount.save(force_update=True)
        super(Receipt, self).save()
        activity = Activity(name="Receipt", date=self.date, addedby_id=self.addedBy_id, amount=self.amount)
        activity.save()