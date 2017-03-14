# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-01 16:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0001_squashed_0026_auto_20161130_2049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='propertyalert',
            name='archive_on',
        ),
        migrations.RemoveField(
            model_name='propertyalert',
            name='silence_on',
        ),
        migrations.RemoveField(
            model_name='propertyalert',
            name='urgency',
        ),
        migrations.AddField(
            model_name='propertyalert',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='propertyalert',
            name='end_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='propertyalert',
            name='modifier',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='propertyalert',
            name='priority',
            field=models.SmallIntegerField(choices=[(1, 'Urgent'), (3, 'High'), (5, 'Medium'), (9, 'Low')], default=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='propertyalert',
            name='start_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='property',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
