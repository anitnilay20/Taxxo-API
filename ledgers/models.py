from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from company.models import Company

Ltype = (
    ("Accounts", "Accounts"),
    ("Inventory", "Inventory"),
)

choices = (
    ("bank OCC AC", "bank OCC AC"),
    ("bank OD AC", "bank OD AC"),
    ("branch Division", "branch Division"),
    ("capital AC", "capital AC"),
    ("cash in hand", "cash in hand"),
    ("current assets", "current assets"),
    ("current liabilities", "current liabilities"),
    ("deposits assets", "deposits assets"),
    ("direct expenses", "direct expenses"),
    ("direct income", "direct income"),
    ("duties n taxes", "duties n taxes"),
    ("expenses direct", "expenses direct"),
    ("expenses indirect", "expenses indirect"),
    ("fixed assets", "fixed assets"),
    ("income direct", "income direct"),
    ("income indirect", "income indirect"),
    ("indirect expenses", "indirect expenses"),
    ("indirect income", "indirect income"),
    ("investments", "investments"),
    ("loans n advances assets", "loans n advances assets"),
    ("loan liability", "loan liability"),
    ("misc exoenses", "misc exoenses"),
    ("provisions", "provisions"),
    ("purchase AC", "purchase AC"),
    ("reserve n surpulus", "reserve n surplus"),
    ("retaines earnings", "retaines earnings"),
    ("sales accounts", "sales accounts"),
    ("secured loans", "secured loans"),
    ("stock in hand", "stock in hand"),
    ("sundry creditors", "sundry creditors"),
    ("sundry debitors", "sundry debitors"),
    ("suspense Account", "suspense Account"),
    ("unsecured loans", "unsecured loans"),
)


class Ledgers(models.Model):
    company = models.ForeignKey(Company)
    name = models.CharField(max_length=1000)
    groups = models.CharField(max_length=1000, choices=choices)
    opening_balance = models.IntegerField(default=0)
    type = models.CharField(max_length=1000, choices=Ltype)
    inventory = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
