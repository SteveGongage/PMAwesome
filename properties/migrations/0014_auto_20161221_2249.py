# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-22 03:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0013_auto_20161221_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='HOA_approvesTenants',
            field=models.BooleanField(default=False, verbose_name='HOA Approves Tenants'),
        ),
        migrations.AlterField(
            model_name='property',
            name='HOA_email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='HOA Email'),
        ),
        migrations.AlterField(
            model_name='property',
            name='HOA_gateCode',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Gate Code'),
        ),
        migrations.AlterField(
            model_name='property',
            name='HOA_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='HOA Name'),
        ),
        migrations.AlterField(
            model_name='property',
            name='HOA_phone',
            field=localflavor.us.models.PhoneNumberField(blank=True, null=True, verbose_name='HOA Phone'),
        ),
        migrations.AlterField(
            model_name='property',
            name='addressCity',
            field=models.CharField(max_length=20, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='property',
            name='addressCounty',
            field=models.CharField(max_length=20, verbose_name='County'),
        ),
        migrations.AlterField(
            model_name='property',
            name='addressShort',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='property',
            name='addressStreet',
            field=models.CharField(help_text='Street name only, no numeric, no unit number.', max_length=30, verbose_name='Street Name'),
        ),
        migrations.AlterField(
            model_name='property',
            name='archived_on',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Archive On'),
        ),
        migrations.AlterField(
            model_name='property',
            name='areaHeatedSqFt',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Heated Area'),
        ),
        migrations.AlterField(
            model_name='property',
            name='areaLotSqFt',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Lot Area'),
        ),
        migrations.AlterField(
            model_name='property',
            name='bathroomsFull',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Full Bathrooms'),
        ),
        migrations.AlterField(
            model_name='property',
            name='bathroomsHalf',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Half Bathrooms'),
        ),
        migrations.AlterField(
            model_name='property',
            name='bedrooms',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Bedrooms'),
        ),
        migrations.AlterField(
            model_name='property',
            name='contactManager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='messaging.Contact', verbose_name='Property Manager'),
        ),
        migrations.AlterField(
            model_name='property',
            name='dateContractStart',
            field=models.DateField(blank=True, null=True, verbose_name='Contract Start Date'),
        ),
        migrations.AlterField(
            model_name='property',
            name='ext_MLSID',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='MLS ID'),
        ),
        migrations.AlterField(
            model_name='property',
            name='ext_appfolioID',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Appfolio ID'),
        ),
        migrations.AlterField(
            model_name='property',
            name='marketingDescription',
            field=models.TextField(blank=True, null=True, verbose_name='Marketing Description'),
        ),
        migrations.AlterField(
            model_name='property',
            name='neighborhood',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='property',
            name='partOfTown',
            field=models.CharField(blank=True, max_length=30, verbose_name='Part of Town'),
        ),
        migrations.AlterField(
            model_name='property',
            name='petCatsOK',
            field=models.BooleanField(default=True, verbose_name='Cats OK?'),
        ),
        migrations.AlterField(
            model_name='property',
            name='petDogsOK',
            field=models.BooleanField(default=True, verbose_name='Dogs OK?'),
        ),
        migrations.AlterField(
            model_name='property',
            name='petRestrictions',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Pet Restrictions'),
        ),
        migrations.AlterField(
            model_name='property',
            name='poolType',
            field=models.CharField(choices=[('none', 'None'), ('private', 'Private'), ('community', 'Community'), ('both', 'Both')], default='none', max_length=10, verbose_name='Pool Type'),
        ),
        migrations.AlterField(
            model_name='property',
            name='propertyType',
            field=models.CharField(choices=[('sfhouse', 'House'), ('condo', 'Condo'), ('townhouse', 'Townhouse'), ('commercial', 'Commercial')], default='sfhouse', max_length=20, verbose_name='Type of Property'),
        ),
        migrations.AlterField(
            model_name='property',
            name='system_excludedItems',
            field=models.CharField(blank=True, help_text='List the areas or items in the home that are excluded from tenant use', max_length=100, null=True, verbose_name='Excluded Items'),
        ),
        migrations.AlterField(
            model_name='property',
            name='system_irrigationController',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Irrigation Controller'),
        ),
        migrations.AlterField(
            model_name='property',
            name='system_irrigationSchedule',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Irrigation Schedule'),
        ),
        migrations.AlterField(
            model_name='property',
            name='system_isSeptic',
            field=models.BooleanField(default=False, verbose_name='On Septic?'),
        ),
        migrations.AlterField(
            model_name='property',
            name='system_isWellWater',
            field=models.BooleanField(default=False, verbose_name='On Well Water?'),
        ),
        migrations.AlterField(
            model_name='property',
            name='system_mainWaterShutoff',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Main Water Shut Off'),
        ),
        migrations.AlterField(
            model_name='property',
            name='system_refrigeratorWaterShutoff',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Refrigerator Water Shut Off'),
        ),
        migrations.AlterField(
            model_name='property',
            name='yearBuilt',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Year Built'),
        ),
    ]
