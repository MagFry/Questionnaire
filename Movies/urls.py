from django.conf.urls import url

from . import views

app_name = 'movie'

urlpatterns = [
    url(r'^movie_list/$', views.movie_list, name='list'),
    url(r'^collect_ratings/$', views.collect_ratings, name='collect_ratings'),
    url(r'^first_movies_category/$', views.first_movies_category, name='first_movies_category'),
    url(r'^index/$', views.index, name='index'),
]
