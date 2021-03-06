# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-29 17:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0004_lockbox'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lockbox',
            name='last_update_contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='messaging.Contact'),
        ),
        migrations.AlterField(
            model_name='lockbox',
            name='prop',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='properties.Property'),
        ),
    ]
