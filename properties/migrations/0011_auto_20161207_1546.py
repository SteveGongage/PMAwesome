# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-07 20:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0010_lease_terms_depositsecurity'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='HOA_approvesTenants',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='HOA_email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='HOA_gateCode',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='HOA_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='HOA_phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='system_excludedItems',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='system_irrigationController',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='system_irrigationSchedule',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='system_isSeptic',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='system_isWellWater',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='system_mainWaterShutoff',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='system_refrigeratorWaterShutoff',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='propertyowner',
            name='isForeignOwner',
            field=models.BooleanField(default=False),
        ),
    ]
