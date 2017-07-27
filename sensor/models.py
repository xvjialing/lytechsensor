# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class TemperatureSensor(models.Model):
    deviceId=models.CharField(max_length=32,unique=True)
    type=models.TextField(null=True)
    maxTemperature=models.FloatField(max_length=32,null=True)
    minTemperature=models.FloatField(max_length=32,null=True)
    create_time=models.DateField(auto_now_add=True,null=True)

    class Meta:
        ordering = ('deviceId',)

    def __unicode__(self):
        return self.deviceId

class TemperatureMsg(models.Model):
    temperature = models.FloatField(max_length=32, null=True)
    pub_time=models.DateField(auto_now_add=True,null=True)
    temperatureSensor=models.ForeignKey(TemperatureSensor)

    class Meta:
        ordering=('temperatureSensor',)

    def __unicode__(self):
        return unicode(self.temperatureSensor)

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



