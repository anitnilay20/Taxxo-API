# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-28 07:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20170528_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='mrp',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='purchase_price',
            field=models.IntegerField(blank=True, default=3),
            preserve_default=False,
        ),
    ]
