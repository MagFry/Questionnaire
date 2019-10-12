from django.conf.urls import url

from . import views

app_name = 'movie'

urlpatterns = [
    url(r'^movie_list/$', views.movie_list, name='list'),
    url(r'^index/$', views.index, name='index'),
]