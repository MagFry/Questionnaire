from django.conf.urls import url

from . import views

app_name = 'responses'

urlpatterns = [
    url(r'^get_csv/$', views.get_csv, name='get_csv'),
]
