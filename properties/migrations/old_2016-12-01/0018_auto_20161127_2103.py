# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-28 02:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0017_auto_20161127_2102'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accessdevice',
            old_name='property',
            new_name='prop',
        ),
        migrations.RenameField(
            model_name='feature',
            old_name='property',
            new_name='prop',
        ),
        migrations.RenameField(
            model_name='vendorservice',
            old_name='property',
            new_name='prop',
        ),
    ]
