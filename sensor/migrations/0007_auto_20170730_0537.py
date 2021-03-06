# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-30 05:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sensor', '0006_auto_20170730_0259'),
    ]

    operations = [
        migrations.CreateModel(
            name='TouchSensorMsg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('pub_time', models.DateField(auto_now_add=True, null=True)),
            ],
            options={
                'ordering': ('touchSensor',),
            },
        ),
        migrations.AlterModelOptions(
            name='touchsensor',
            options={'ordering': ('deviceId',)},
        ),
        migrations.AddField(
            model_name='touchsensor',
            name='create_time',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='touchsensor',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='touchsensor',
            name='type',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='touchsensormsg',
            name='touchSensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='touchSensorMsgs', to='sensor.TouchSensor'),
        ),
    ]
