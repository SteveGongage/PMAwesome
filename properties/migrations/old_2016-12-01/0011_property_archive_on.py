# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-18 02:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0010_auto_20161117_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='archive_on',
            field=models.DateTimeField(blank=True, null=True),
            preserve_default=False,
        ),
    ]