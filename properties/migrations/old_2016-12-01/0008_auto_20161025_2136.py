# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-26 01:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0007_auto_20161024_2155'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]