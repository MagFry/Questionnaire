from django.conf.urls import url

from . import views

app_name = 'movie'

urlpatterns = [
    url(r'^movie_list/$', views.movie_list, name='list'),
    url(r'^horror_movies/$', views.horror_movies, name='horror'),
    url(r'^mystery_movies/$', views.mystery_movies, name='mystery'),
    url(r'^index/$', views.index, name='index'),
]