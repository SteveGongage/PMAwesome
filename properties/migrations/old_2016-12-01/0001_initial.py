# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-24 23:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('addressNumeric', models.IntegerField()),
                ('addressStreet', models.CharField(max_length=50)),
                ('addressUnit', models.CharField(blank=True, max_length=20)),
                ('addressCity', models.CharField(max_length=30)),
                ('addressState', models.CharField(max_length=20)),
                ('addressZipcode', models.CharField(max_length=10)),
                ('addressCounty', models.CharField(max_length=30)),
                ('addressFull', models.CharField(max_length=100)),
                ('addressStreet1', models.CharField(blank=True, max_length=50)),
                ('addressStreet2', models.CharField(blank=True, max_length=50)),
                ('neighborhood', models.CharField(blank=True, max_length=50)),
                ('partOfTown', models.CharField(blank=True, max_length=50)),
                ('isMapable', models.BooleanField(default=False)),
                ('mapNotes', models.TextField(blank=True)),
                ('mapLatitude', models.FloatField(null=True)),
                ('mapLongitude', models.FloatField(null=True)),
                ('areaHeatedSqFt', models.IntegerField(null=True)),
                ('areaLotSqFt', models.IntegerField(null=True)),
                ('bedrooms', models.IntegerField(null=True)),
                ('bathroomsFull', models.IntegerField(null=True)),
                ('bathroomsHalf', models.IntegerField(null=True)),
                ('yearBuilt', models.IntegerField(null=True)),
                ('poolType', models.CharField(choices=[('none', 'none'), ('private', 'private'), ('community', 'community'), ('both', 'both')], default='none', max_length=10)),
            ],
        ),
    ]
