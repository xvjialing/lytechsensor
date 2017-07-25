# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import TemperatureSensor, FlameSensor,HeartbeatSensor,HallMagneticSensor,SoundSensor,TouchSensor,HumiditySensor,InfraredSensor,LightSensor,VibrationSensor
from .models import Task
from serializers import TemperatureSerializer,TaskSerializer
from rest_framework.decorators import api_view, permission_classes
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

@api_view(['GET','POST'])
@permission_classes()

# 第三种方式：装饰器 api_view
@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def task_list(request):
    '''
    List all tasks, or create a new task.
    '''
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def task_detail(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
