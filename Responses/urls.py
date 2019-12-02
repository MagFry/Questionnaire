from django.conf.urls import url

from . import views

app_name = 'responses'

urlpatterns = [
    url(r'^get_csv/$', views.get_csv, name='get_csv'),
    url(r'^get_csv2/$', views.get_csv_curl_friendly, name='get_csv_curl_friendly'),
    url(r'^get_all_csv/$', views.get_all_csv, name='get_all_csv'),
    url(r'^db_repopulate/$', views.db_repopulate, name='db_repopulate'),
]
