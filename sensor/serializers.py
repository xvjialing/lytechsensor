from rest_framework import serializers
from .models import TemperatureSensor,FlameSensor,HeartbeatSensor,HallMagneticSensor,SoundSensor,TouchSensor
from .models import TemperatureMsg,FlameMsg,HeartbeatMsg,HallSensorMsg,SoundSensorMsg,TouchSensorMsg
from django.contrib.auth.models import User

# class TemperatureSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=TemperatureSensor
#         fields=('id','deviceId','temperature','maxTemperature','minTemperature','pub_time')


# class TaskSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Task
#         fields = ('id', 'title', 'description', 'completed', 'create_date')


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username','password','email')


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







