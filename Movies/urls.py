from django.conf.urls import url

from . import views

app_name = 'movie'

urlpatterns = [
    url(r'^test_rating/$', views.test_rating, name='test_rating'),
    url(r'^insert_rating/$', views.insert_rating, name='insert_rating'),
    url(r'^rating/$', views.rating, name='rating'),
]
