# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-25 01:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0004_auto_20161024_2117'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameFirst', models.CharField(max_length=30)),
                ('nameLast', models.CharField(max_length=30)),
                ('nameMiddle', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fromEmail', models.CharField(max_length=254)),
                ('fromEmailName', models.CharField(max_length=100)),
                ('fromContact', models.IntegerField()),
                ('cc', models.CharField(max_length=1000)),
                ('bcc', models.CharField(max_length=1000)),
                ('subject', models.CharField(max_length=80)),
                ('message', models.TextField(blank=True)),
                ('propertyID', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
