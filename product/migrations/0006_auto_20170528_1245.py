# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-28 07:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20170528_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='location',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]