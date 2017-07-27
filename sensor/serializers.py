from rest_framework import serializers
from .models import TemperatureSensor,Task

# class TemperatureSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=TemperatureSensor
#         fields=('id','deviceId','temperature','maxTemperature','minTemperature','pub_time')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'completed', 'create_date')


