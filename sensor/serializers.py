from rest_framework import serializers
from .models import TemperatureSensor,FlameSensor,HeartbeatSensor,HallMagneticSensor,SoundSensor,TouchSensor,HumiditySensor
from .models import TemperatureMsg,FlameMsg,HeartbeatMsg,HallSensorMsg,SoundSensorMsg,TouchSensorMsg,HumiditySensorMsg
import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class TemperatureMsgSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemperatureMsg
        fields = ('id', 'temperature', 'pub_time', 'temperatureSensor')


class TemperatureSensorSerializer(serializers.ModelSerializer):
    temperatureMsgs = TemperatureMsgSerializer(many=True, read_only=True)

    class Meta:
        model = TemperatureSensor
        fields = ('id', 'deviceId', 'type', 'maxTemperature', 'minTemperature', 'create_time', 'temperatureMsgs')
        

class FlameMsgSerializer(serializers.ModelSerializer):
    class Meta:
        model=FlameMsg
        fields=('id','wavelength','pub_time','status','flameSensor')

class FlameSensorSerializer(serializers.ModelSerializer):
    temperatureMsgs=FlameMsgSerializer(many=True, read_only=True)
    class Meta:
        model = FlameSensor
        fields = ('id', 'deviceId', 'type', 'max_wavelength','create_time','status','temperatureMsgs')

class HeartbeatMsgSerializer(serializers.ModelSerializer):
    class Meta:
        model=HeartbeatMsg
        fields=('id','heartRate','status','pub_time','heartbeatSensor')

class HeartbeatSensorSerializer(serializers.ModelSerializer):
    heartbeatMsgs=HeartbeatMsgSerializer(many=True,read_only=True)
    class Meta:
        model=HeartbeatSensor
        fields=('id','deviceId','status','type','create_time','heartbeatMsgs')

class HallSensorMsgSerializer(serializers.ModelSerializer):
    class Meta:
        model=HallSensorMsg
        fields=('id','MagnetiStrength','status','pub_time','hallMagneticSensor')

class HallMagneticSensorSerializer(serializers.ModelSerializer):
    hallSensorMsgs=HallSensorMsgSerializer(many=True,read_only=True)

    class Meta:
        model=HallMagneticSensor
        fields=('id','deviceId','SettingMagnetic','type','status','create_time','hallSensorMsgs')

class SoundSensorMsgSerializer(serializers.ModelSerializer):
    class Meta:
        model=SoundSensorMsg
        fields=('id','xAxis','yAxis','status','pub_time','soundSensor')

class SoundSensorSerializer(serializers.ModelSerializer):
    soundSensorMsgs=SoundSensorMsgSerializer(many=True,read_only=True)

    class Meta:
        model=SoundSensor
        fields=('id','deviceId','type','status','create_time','soundSensorMsgs')


class TouchSensorMsgSerializer(serializers.ModelSerializer):
    class Meta:
        model=TouchSensorMsg
        fields=('id','status','pub_time','touchSensor')

class TouchSensorSerializer(serializers.ModelSerializer):
    touchSensorMsgs=TouchSensorMsgSerializer(many=True,read_only=True)

    class Meta:
        model=TouchSensor
        fields=('id','deviceId','type','status','create_time','touchSensorMsgs')


class TiltSensorMsgSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.TiltSensorMsg
        fields=('id','status','pub_time','tiltSensor')

class TiltSensorSerializer(serializers.ModelSerializer):
    tiltSensorMsgs=TiltSensorMsgSerializer(many=True,read_only=True)

    class Meta:
        model=models.TiltSensor
        fields=('id','deviceId','type','status','create_time','tiltSensorMsgs')


class HumiditySensorMsgSerializer(serializers.ModelSerializer):
    class Meta:
        model=HumiditySensorMsg
        fields=('id','humidity','status','pub_time','humiditySensor')

class HumiditySensorSerializer(serializers.ModelSerializer):
    humiditySensorMsgs=HumiditySensorMsgSerializer(many=True,read_only=True)

    class Meta:
        model=HumiditySensor
        fields=('id','deviceId','type','status','create_time','humiditySensorMsgs')


class InfraredSensorMsgSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.InfraredSensorMsg
        fields=('id','status','pub_time','infraredSensor')

class InfraredSensorSerializer(serializers.ModelSerializer):
    infraredSensorMsgs=InfraredSensorMsgSerializer(many=True,read_only=True)

    class Meta:
        model=models.InfraredSensor
        fields=('id','deviceId','type','status','create_time','infraredSensorMsgs')


class LightSensorMsgSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.LightSensorMsg
        fields=('id','status','lightIntensity','pub_time','lightSensor')

class LightSensorSerializer(serializers.ModelSerializer):
    lightSensorMsgs=LightSensorMsgSerializer(many=True,read_only=True)

    class Meta:
        model=models.LightSensor
        fields=('id','deviceId','type','status','create_time','lightSensorMsgs')


class VibrationSensorMsgSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.VibrationSensorMsg
        fields=('id','xAxis','yAxis','status','pub_time','vibrationSensor')

class VibrationSensorSerializer(serializers.ModelSerializer):
    vibrationSensorMsgs=VibrationSensorMsgSerializer(many=True,read_only=True)

    class Meta:
        model=models.VibrationSensor
        fields=('id','deviceId','type','status','create_time','vibrationSensorMsgs')

class SwitchSensorMsgSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.SwitchSensorMsg
        fields=('id','status','pub_time','switchSensor')

class SwitchSensorSerializer(serializers.ModelSerializer):
    switchSensorMsgs=SwitchSensorMsgSerializer(many=True,read_only=True)

    class Meta:
        model=models.SwitchSensor
        fields=('id','deviceId','type','status','create_time','switchSensorMsgs')









