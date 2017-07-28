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
    url(r'^flameSensors/$', views.TemperatureSensorList.as_view(), name='flameSensor_list'),
    url(r'^flameSensors/(?P<pk>[0-9]+)$', views.TemperatureSensorDetail.as_view(), name='flameSensor_detail'),
    # url(r'^users/$', views.UserList.as_view(), name='user_list'),
    # url(r'^users/(?P<pk>[0-9]+)$', views.UserDetail.as_view(), name='user_detail'),
    url(r'^register/$',views.register,name='register'),
    url(r'^api-token-auth/', authViews.obtain_auth_token),
    url(r'^$', schema_view),
]
