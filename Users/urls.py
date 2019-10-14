from django.conf.urls import url

from . import views

app_name = 'user'

urlpatterns = [
    url(r'', views.get_name, name='name'),
]