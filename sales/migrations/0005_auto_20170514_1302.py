# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-14 07:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0004_sales_total_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sales',
            name='Invoice',
        ),
        migrations.AddField(
            model_name='sales',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
