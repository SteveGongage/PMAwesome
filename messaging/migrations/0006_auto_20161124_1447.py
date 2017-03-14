# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-24 19:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0005_auto_20161116_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='dateOfBirth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='driversLicenseNumber',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='driversLicenseState',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='email1',
            field=models.CharField(blank=True, max_length=52, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='email1_type',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='email2',
            field=models.CharField(blank=True, max_length=52, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='email2_type',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone1',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone1_type',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone2_type',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone3',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone3_type',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='salutation',
            field=models.CharField(choices=[('', ''), ('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Ms', 'Ms'), ('Miss', 'Miss'), ('Dr', 'Dr'), ('Mx', 'Mx')], default='Mr', max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='ssn',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]
