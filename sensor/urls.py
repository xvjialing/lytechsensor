from django.conf.urls import url,include

from . import views
from rest_framework.authtoken import views as authViews
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='LYTECH SENSOR API')

urlpatterns = [
    # url(r'^temperature/$', views.TemperatureList),
    # url(r'^temperature/(?P<pk>[0-9]+)$', views.TemperatureDetail),
    # url(r'^tasks/$', views.TaskList.as_view(), name='task_list'),
    # url(r'^tasks/(?P<pk>[0-9]+)$', views.TaskDetail.as_view(), name='task_detail'),
    url(r'^temperatureSensors/$', views.TemperatureSensorList.as_view(), name='temperatureSensor_list'),
    url(r'^temperatureSensors/(?P<pk>[0-9]+)$', views.TemperatureSensorDetail.as_view(), name='temperatureSensor_detail'),

    url(r'^temperatureMsgs/$', views.TemperatureMsgList.as_view(), name='temperatureMsg_list'),
    url(r'^temperatureMsgs/(?P<pk>[0-9]+)$', views.TemperatureMsgDetail.as_view(), name='temperatureMsg_detail'),

    url(r'^flameSensors/$', views.FlameSensorList.as_view(), name='flameSensor_list'),
    url(r'^flameSensors/(?P<pk>[0-9]+)$', views.FlameSensorDetail.as_view(), name='flameSensor_detail'),

    url(r'^flameMsgs/$', views.FlameMsgList.as_view(), name='flameMsg_list'),
    url(r'^flameMsgs/(?P<pk>[0-9]+)$', views.FlameMsgDetail.as_view(), name='flameMsg_detail'),

    url(r'^heartbeatSensors/$', views.HeartbeatSensorList.as_view(), name='heartbeatSensor_list'),
    url(r'^heartbeatSensors/(?P<pk>[0-9]+)$', views.HeartbeatSensorDetail.as_view(), name='heartbeatSensor_detail'),

    url(r'^heartbeatMsgs/$', views.HeartbeatMsgList.as_view(), name='heartbeatMsg_list'),
    url(r'^heartbeatMsgs/(?P<pk>[0-9]+)$', views.HeartbeatMsgDetail.as_view(), name='heartbeatMsg_detail'),

    url(r'^hallMagneticSensors/$', views.HallMagneticSensorList.as_view(), name='hallMagneticSensor_list'),
    url(r'^hallMagneticSensors/(?P<pk>[0-9]+)$', views.HallMagneticSensorDetail.as_view(), name='hallMagneticSensor_detail'),

    url(r'^hallSensorMsgs/$', views.HallSensorMsgList.as_view(), name='hallSensorMsg_list'),
    url(r'^hallSensorMsgs/(?P<pk>[0-9]+)$', views.HallSensorMsgDetail.as_view(), name='hallSensorMsg_detail'),

    url(r'^soundSensors/$', views.SoundSensorList.as_view(), name='soundSensor_list'),
    url(r'^soundSensors/(?P<pk>[0-9]+)$', views.SoundSensorDetail.as_view(), name='soundSensor_detail'),

    url(r'^soundSensorMsgs/$', views.SoundSensorMsgList.as_view(), name='soundSensorMsg_list'),
    url(r'^soundSensorMsgs/(?P<pk>[0-9]+)$', views.SoundSensorMsgDetail.as_view(), name='soundSensorMsg_detail'),

    url(r'^touchSensors/$', views.TouchSensorList.as_view(), name='touchSensor_list'),
    url(r'^touchSensors/(?P<pk>[0-9]+)$', views.TouchSensorDetail.as_view(), name='touchSensor_detail'),

    url(r'^touchSensorMsgs/$', views.TouchSensorMsgList.as_view(), name='touchSensorMsg_list'),
    url(r'^touchSensorMsgs/(?P<pk>[0-9]+)$', views.TouchSensorMsgDetail.as_view(), name='touchSensorMsg_detail'),

    url(r'^tiltSensors/$', views.TiltSensorList.as_view(), name='tiltSensor_list'),
    url(r'^tiltSensors/(?P<pk>[0-9]+)$', views.TiltSensorDetail.as_view(), name='tiltSensor_detail'),

    url(r'^tiltSensorMsgs/$', views.TiltSensorMsgList.as_view(), name='tiltSensorMsg_list'),
    url(r'^tiltSensorMsgs/(?P<pk>[0-9]+)$', views.TiltSensorMsgDetail.as_view(), name='tiltSensorMsg_detail'),

    url(r'^humiditySensors/$', views.HumiditySensorList.as_view(), name='humiditySensor_list'),
    url(r'^humiditySensors/(?P<pk>[0-9]+)$', views.HumiditySensorDetail.as_view(), name='humiditySensor_detail'),

    url(r'^humiditySensorMsgs/$', views.HumiditySensorMsgList.as_view(), name='humiditySensorMsg_list'),
    url(r'^humiditySensorMsgs/(?P<pk>[0-9]+)$', views.HumiditySensorMsgDetail.as_view(), name='humiditySensorMsg_detail'),


    url(r'^infraredSensors/$', views.InfraredSensorList.as_view(), name='infraredSensor_list'),
    url(r'^infraredSensors/(?P<pk>[0-9]+)$', views.InfraredSensorDetail.as_view(), name='infraredSensor_detail'),

    url(r'^infraredSensorMsgs/$', views.InfraredSensorMsgList.as_view(), name='infraredSensorMsg_list'),
    url(r'^infraredSensorMsgs/(?P<pk>[0-9]+)$', views.InfraredSensorMsgDetail.as_view(), name='infraredSensorMsg_detail'),


    url(r'^lightSensors/$', views.LightSensorList.as_view(), name='lightSensor_list'),
    url(r'^lightSensors/(?P<pk>[0-9]+)$', views.LightSensorDetail.as_view(), name='lightSensor_detail'),

    url(r'^lightSensorMsgs/$', views.LightSensorMsgList.as_view(), name='lightSensorMsg_list'),
    url(r'^lightSensorMsgs/(?P<pk>[0-9]+)$', views.LightSensorMsgDetail.as_view(), name='lightSensorMsg_detail'),


    url(r'^vibrationSensors/$', views.VibrationSensorList.as_view(), name='vibrationSensor_list'),
    url(r'^vibrationSensors/(?P<pk>[0-9]+)$', views.VibrationSensorDetail.as_view(), name='vibrationSensor_detail'),

    url(r'^vibrationSensorMsgs/$', views.VibrationSensorMsgList.as_view(), name='vibrationSensorMsg_list'),
    url(r'^vibrationSensorMsgs/(?P<pk>[0-9]+)$', views.VibrationSensorMsgDetail.as_view(), name='vibrationSensorMsg_detail'),


    url(r'^switchSensors/$', views.SwitchSensorList.as_view(), name='switchSensor_list'),
    url(r'^switchSensors/(?P<pk>[0-9]+)$', views.SwitchSensorDetail.as_view(), name='switchSensor_detail'),

    url(r'^switchSensorMsgs/$', views.SwitchSensorMsgList.as_view(), name='switchSensorMsg_list'),
    url(r'^switchSensorMsgs/(?P<pk>[0-9]+)$', views.SwitchSensorMsgDetail.as_view(), name='switchSensorMsg_detail'),

    # url(r'^users/$', views.UserList.as_view(), name='user_list'),
    # url(r'^users/(?P<pk>[0-9]+)$', views.UserDetail.as_view(), name='user_detail'),
    url(r'^register/$',views.register,name='register'),
    url(r'^api-token-auth/', authViews.obtain_auth_token),
    url(r'^$', schema_view),
]
