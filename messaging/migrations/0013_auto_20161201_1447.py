# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-01 19:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0005_auto_20161201_1425'),
        ('messaging', '0012_auto_20161201_1425'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='propertyID',
        ),
        migrations.AddField(
            model_name='contact',
            name='approvedByHuman',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='autoGenerated',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='isArchived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='message',
            name='prop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='properties.Property'),
        ),
        migrations.AddField(
            model_name='thread',
            name='isArchived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='thread',
            name='priority',
            field=models.PositiveSmallIntegerField(choices=[(100, 'Urgent'), (80, 'High'), (60, 'Medium'), (40, 'Low'), (20, 'Info'), (10, 'System Log')], default=60),
        ),
        migrations.AlterField(
            model_name='message',
            name='isNew',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='thread',
            name='assignedToContactID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='threads_assigned', to='messaging.Contact'),
        ),
        migrations.AlterField(
            model_name='thread',
            name='propertyID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.Property'),
        ),
        migrations.AlterField(
            model_name='thread',
            name='requesterContactID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='threads_requestor', to='messaging.Contact'),
        ),
    ]
