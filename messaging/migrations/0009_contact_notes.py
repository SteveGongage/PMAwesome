# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-29 21:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0008_auto_20161129_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]