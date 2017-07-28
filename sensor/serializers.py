from rest_framework import serializers
from .models import TemperatureSensor, TemperatureMsg, Task, FlameSensor
from django.contrib.auth.models import User



# class TemperatureSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=TemperatureSensor
#         fields=('id','deviceId','temperature','maxTemperature','minTemperature','pub_time')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'completed', 'create_date')


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



class FlameSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlameSensor
        fields = ('id', 'deviceId', 'type', 'create_time')
