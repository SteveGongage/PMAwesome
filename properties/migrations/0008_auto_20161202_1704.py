# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-02 22:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0007_auto_20161202_1704'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leasecontact',
            old_name='isFinancialyResponsible',
            new_name='isFinanciallyResponsible',
        ),
    ]