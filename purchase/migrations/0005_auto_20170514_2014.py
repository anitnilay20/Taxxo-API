# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-14 14:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0012_auto_20170514_1255'),
        ('purchase', '0004_auto_20170514_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='company.Company'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchase',
            name='narration',
            field=models.CharField(default=' ', max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='purchase',
            name='journals',
            field=models.ManyToManyField(related_name='Purchase_journal', to='journal.Journal'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='party_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ledgers.Ledgers'),
        ),
    ]