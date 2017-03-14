# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-27 20:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0014_auto_20161127_1453'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fee',
            old_name='archive_at',
            new_name='archived_at',
        ),
        migrations.RenameField(
            model_name='property',
            old_name='archive_on',
            new_name='archived_at',
        ),
        migrations.AddField(
            model_name='lease',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
    ]