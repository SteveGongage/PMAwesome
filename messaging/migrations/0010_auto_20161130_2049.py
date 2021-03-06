# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-01 01:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0009_contact_notes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='created_at',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='updated_at',
            new_name='updated_on',
        ),
        migrations.RenameField(
            model_name='thread',
            old_name='created_at',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='thread',
            old_name='updated_at',
            new_name='updated_on',
        ),
    ]
