# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-01 19:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0012_auto_20161201_1425'),
        ('properties', '0004_auto_20161201_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertyactivity',
            name='message',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='messaging.Message'),
        ),
        migrations.AlterField(
            model_name='propertyactivity',
            name='priority',
            field=models.PositiveSmallIntegerField(choices=[(100, 'Urgent'), (80, 'High'), (60, 'Medium'), (40, 'Low'), (20, 'Info'), (10, 'System Log')], default=60),
        ),
        migrations.AlterField(
            model_name='propertyactivity',
            name='type',
            field=models.CharField(choices=[('lease expiring', 'Lease Expiring'), ('moving out', 'Moving Out'), ('vacant', 'Vacant'), ('tenants needed', 'Tenants Needed'), ('incident', 'Incident'), ('rent late', 'Rent Late'), ('eviction', 'Eviction'), ('tenant issue', 'Tenant Issue'), ('owner issue', 'Owner Issue'), ('info incomplete', 'Incomplete Info'), ('rent paid', 'Rent Paid'), ('inspection', 'Inspection'), ('service performed', 'Service Performed')], max_length=24),
        ),
    ]
