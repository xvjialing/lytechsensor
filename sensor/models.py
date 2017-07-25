# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class TemperatureSensor(models.Model):
    deviceId=models.CharField(max_length=32,unique=True)
    temperature=models.FloatField(max_length=32,null=True)
    maxTemperature=models.FloatField(max_length=32,null=True)
    minTemperature=models.FloatField(max_length=32,null=True)
    pub_time=models.DateField(auto_now_add=True,null=True)

    class Meta:
        ordering = ('deviceId',)

    def __unicode__(self):
        return self.deviceId

class FlameSensor(models.Model):
    deviceId = models.CharField(max_length=32, unique=True)

    def __unicode__(self):
        return self.deviceId

class HeartbeatSensor(models.Model):
    deviceId = models.CharField(max_length=32, unique=True)

    def __unicode__(self):
        return self.deviceId

class HallMagneticSensor(models.Model):
    deviceId = models.CharField(max_length=32, unique=True)
    magnetic =models.FloatField

    def __unicode__(self):
        return self.deviceId

class SoundSensor(models.Model):
    deviceId = models.CharField(max_length=32, unique=True)

    def __unicode__(self):
        return self.deviceId

class TouchSensor(models.Model):
    deviceId = models.CharField(max_length=32, unique=True)

    def __unicode__(self):
        return  self.deviceId

class HumiditySensor(models.Model):
    deviceId = models.CharField(max_length=32, unique=True)

    def __unicode__(self):
        return self.deviceId

class InfraredSensor(models.Model):
    deviceId = models.CharField(max_length=32, unique=True)

    def __unicode__(self):
        return self.deviceId

class LightSensor(models.Model):
    deviceId = models.CharField(max_length=32, unique=True)

    def __unicode__(self):
        return self.deviceId

class VibrationSensor(models.Model):
    deviceId = models.CharField(max_length=32, unique=True)

    def __unicode__(self):
        return self.deviceId

class Task(models.Model):
    title = models.CharField('标题', max_length=100)
    description = models.TextField('描述')
    completed = models.BooleanField('是否完成', default=False)
    create_date = models.DateTimeField('创建时间', auto_now_add=True)

    def __unicode__(self):
        return self.title



