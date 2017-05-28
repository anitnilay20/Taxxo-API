from __future__ import unicode_literals
from django.db import models
from company.models import Company
from Customer.models import Profile


class Product(models.Model):
    name = models.CharField(max_length=1000)
    company = models.ForeignKey(Company)
    rate = models.IntegerField()
    discount = models.IntegerField(blank=True)
    batch_no = models.IntegerField(blank=True)
    manufacturing_date = models.DateField(blank=True)
    expiry_date = models.DateField(blank=True)
    tax = models.IntegerField()
    location = models.CharField(max_length=1000,blank=True)
    manufacturing_company = models.CharField(max_length=1000)
    mrp = models.IntegerField()
    purchase_price = models.IntegerField()
    hsn_code = models.IntegerField()
    sac_code = models.IntegerField(blank=True)
    added_by = models.ForeignKey(Profile)
