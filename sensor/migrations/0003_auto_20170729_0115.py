# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-29 01:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sensor', '0002_auto_20170729_0054'),
    ]

    operations = [
        migrations.AddField(
            model_name='flamesensor',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='flamemsg',
            name='flameSensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flameMsgs', to='sensor.FlameSensor'),
        ),
    ]