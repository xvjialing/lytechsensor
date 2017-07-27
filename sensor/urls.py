from django.conf.urls import url,include

from . import views
from rest_framework.authtoken import views as authViews
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='LYTECH SENSOR API')

urlpatterns = [
    # url(r'^temperature/$', views.TemperatureList),
    # url(r'^temperature/(?P<pk>[0-9]+)$', views.TemperatureDetail),
    url(r'^tasks/$', views.TaskList.as_view(), name='task_list'),
    url(r'^tasks/(?P<pk>[0-9]+)$', views.TaskDetail.as_view(), name='task_detail'),
    url(r'^api-token-auth/', authViews.obtain_auth_token),
    url(r'^$', schema_view),
]
