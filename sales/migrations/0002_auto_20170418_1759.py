# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-18 12:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Purchase',
            new_name='Sales',
        ),
    ]
