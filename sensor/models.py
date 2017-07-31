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
    temperatureSensor=models.ForeignKey(TemperatureSensor, related_name='temperatureMsgs')

    class Meta:
        ordering=('temperatureSensor',)

    def __unicode__(self):
        return unicode(self.temperatureSensor)

class FlameSensor(models.Model):
    deviceId = models.CharField(max_length=32, unique=True)
    type = models.TextField(null=True)
    max_wavelength=models.FloatField(null=True)
    status = models.BooleanField(default=False)
    create_time = models.DateField(auto_now_add=True, null=True)

    def __unicode__(self):
        return self.deviceId

    class Meta:
        ordering=('deviceId',)

class FlameMsg(models.Model):
    wavelength=models.FloatField(null=True)
    pub_time = models.DateField(auto_now_add=True, null=True)
    status=models.BooleanField(default=False)
    flameSensor=models.ForeignKey(FlameSensor, related_name='flameMsgs')

    class Meta:
        ordering=('flameSensor',)

    def __unicode__(self):
        return unicode(self.flameSensor)

class HeartbeatSensor(models.Model):
    deviceId = models.CharField(max_length=32, unique=True)
    status=models.BooleanField(default=False)
    type = models.TextField(null=True)
    create_time = models.DateField(auto_now_add=True, null=True)

    class Meta:
        ordering=('deviceId',)

    def __unicode__(self):
        return self.deviceId

class HeartbeatMsg(models.Model):
    heartRate=models.FloatField(null=False)
    status=models.BooleanField(default=False)
    pub_time = models.DateField(auto_now_add=True, null=True)
    heartbeatSensor = models.ForeignKey(HeartbeatSensor, related_name='heartbeatMsgs')

    class Meta:
        ordering=('heartbeatSensor',)

    def __unicode__(self):
        return unicode(self.heartbeatSensor)

class HallMagneticSensor(models.Model):
    deviceId = models.CharField(max_length=32, unique=True)
    SettingMagnetic =models.FloatField(null=True)
    type = models.TextField(null=True)
    status = models.BooleanField(default=False)
    create_time = models.DateField(auto_now_add=True, null=True)

    class Meta:
        ordering=('deviceId',)

    def __unicode__(self):
        return self.deviceId

class HallSensorMsg(models.Model):
    MagnetiStrength = models.FloatField(null=False)
    status = models.BooleanField(default=False)
    pub_time = models.DateField(auto_now_add=True, null=True)
    hallMagneticSensor=models.ForeignKey(HallMagneticSensor,related_name='hallSensorMsgs')

    class Meta:
        ordering=('hallMagneticSensor',)

    def __unicode__(self):
        return unicode(self.hallMagneticSensor)

class SoundSensor(models.Model):
    deviceId = models.CharField(max_length=32, unique=True)
    type = models.TextField(null=True)
    status = models.BooleanField(default=False)
    create_time = models.DateField(auto_now_add=True, null=True)

    class Meta:
        ordering=('deviceId',)

    def __unicode__(self):
        return self.deviceId


class SoundSensorMsg(models.Model):
    xAxis=models.FloatField(null=False)
    yAxis=models.FloatField(null=False)
    status = models.BooleanField(default=False)
    pub_time = models.DateField(auto_now_add=True, null=True)
    soundSensor=models.ForeignKey(SoundSensor,related_name='soundSensorMsgs')

    class Meta:
        ordering=('soundSensor',)

    def __unicode__(self):
        return unicode(self.soundSensor)

class TouchSensor(models.Model):
    deviceId = models.CharField(max_length=32, unique=True)
    type = models.TextField(null=True)
    status = models.BooleanField(default=False)
    create_time = models.DateField(auto_now_add=True, null=True)

    class Meta:
        ordering=('deviceId',)

    def __unicode__(self):
        return  self.deviceId

class TouchSensorMsg(models.Model):
    status = models.BooleanField(default=False)
    pub_time = models.DateField(auto_now_add=True, null=True)
    touchSensor=models.ForeignKey(TouchSensor,related_name='touchSensorMsgs')

    class Meta:
        ordering=('touchSensor',)

    def __unicode__(self):
        return unicode(self.touchSensor)

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



