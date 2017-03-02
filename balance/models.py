from __future__ import unicode_literals
from django.db import models
from company.models import Company


class Balance(models.Model):
    company = models.ForeignKey(Company)
    type = models.CharField(max_length=20)
    amount = models.IntegerField()
