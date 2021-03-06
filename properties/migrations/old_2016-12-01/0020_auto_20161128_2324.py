# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-29 04:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0006_auto_20161124_1447'),
        ('properties', '0019_auto_20161128_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='contactManager',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='messaging.Contact', null=True, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='property',
            name='dateContractStart',
            field=models.DateField(auto_now=True),
        ),
    ]
