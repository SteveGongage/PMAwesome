# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-29 17:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0002_auto_20161229_1201'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservedkey',
            old_name='last_used_contact',
            new_name='last_update_contact',
        ),
        migrations.RenameField(
            model_name='reservedkey',
            old_name='last_used_date',
            new_name='last_update_date',
        ),
        migrations.RenameField(
            model_name='reservedkey',
            old_name='last_used_location',
            new_name='location',
        ),
    ]
