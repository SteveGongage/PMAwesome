# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-22 02:36
from __future__ import unicode_literals

from django.db import migrations, models
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0011_auto_20161207_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lease',
            name='terms_depositSecurity',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='lease',
            name='terms_feeLate',
            field=models.PositiveIntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='lease',
            name='terms_feeLateNotice',
            field=models.PositiveIntegerField(default=25),
        ),
        migrations.AlterField(
            model_name='property',
            name='addressCity',
            field=models.CharField(max_length=30, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='property',
            name='addressNumeric',
            field=models.PositiveIntegerField(help_text='Number only', verbose_name='Street Numeric'),
        ),
        migrations.AlterField(
            model_name='property',
            name='addressState',
            field=localflavor.us.models.USStateField(verbose_name='State'),
        ),
        migrations.AlterField(
            model_name='property',
            name='addressStreet',
            field=models.CharField(help_text='Street name only, no numeric, no unit number.', max_length=50, verbose_name='Street Name'),
        ),
        migrations.AlterField(
            model_name='property',
            name='addressUnit',
            field=models.CharField(blank=True, max_length=20, verbose_name='Unit'),
        ),
        migrations.AlterField(
            model_name='propertyactivity',
            name='type',
            field=models.CharField(choices=[('lease expiring', 'Lease Expiring'), ('lease signed', 'Lease Signed'), ('moving out', 'Moving Out'), ('moving in', 'Moving Out'), ('vacant', 'Vacant'), ('tenants needed', 'Tenants Needed'), ('work order', 'Work Order'), ('service request', 'Service Request'), ('incident', 'Incident'), ('rent late', 'Rent Paid Late'), ('eviction', 'Eviction'), ('official notice', 'Official Notice'), ('violation', 'Violation'), ('tenant', 'Tenant Issue'), ('owner', 'Owner Issue'), ('info incomplete', 'Info Incomplete'), ('info', 'Information'), ('rent paid', 'Rent Paid'), ('inspection', 'Inspection'), ('service', 'Service')], max_length=24),
        ),
    ]
