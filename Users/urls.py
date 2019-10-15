from django.conf.urls import url

from . import views

app_name = 'user'

urlpatterns = [
    url(r'', views.get_name, name='name'),
    url(r'^users/wrong_name', views.get_name, name='wrong_name'),
    url(r'^users/empty_name', views.get_name, name='empty_name'),
]