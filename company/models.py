from __future__ import unicode_literals
from django.db import models
from Customer.models import Profile


class Company(models.Model):
    alias_name = models.CharField(max_length=1000)
    name = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)
    country = models.CharField(max_length=1000)
    city = models.CharField(max_length=1000)
    pin_code = models.IntegerField()
    telephone_number = models.IntegerField()
    email = models.CharField(max_length=1000)
    currency_symbols = models.CharField(max_length=1000)
    accounts_with_inventory = models.BooleanField()
    financial_year_from = models.DateField()
    books_beginning_from = models.DateField()
    show_amounts_in_millions = models.BooleanField()
    admin = models.ForeignKey(Profile)

