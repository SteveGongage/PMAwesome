# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-28 02:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0016_auto_20161127_2029'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lease',
            old_name='property',
            new_name='prop',
        ),
        migrations.RemoveField(
            model_name='lease',
            name='terms_depositPet',
        ),
        migrations.RemoveField(
            model_name='lease',
            name='terms_depositSecurity',
        ),
        migrations.RemoveField(
            model_name='lease',
            name='terms_feeCarpet',
        ),
        migrations.RemoveField(
            model_name='lease',
            name='terms_feeCleaning',
        ),
        migrations.RemoveField(
            model_name='lease',
            name='terms_feeLate',
        ),
        migrations.RemoveField(
            model_name='lease',
            name='terms_feeLateNotice',
        ),
        migrations.RemoveField(
            model_name='lease',
            name='terms_feePet',
        ),
        migrations.RemoveField(
            model_name='lease',
            name='terms_feeRenewal',
        ),
    ]
