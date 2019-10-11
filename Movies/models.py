from django.db import models

# Create your models here.


class Movies(models.Model):
    movie_id = models.IntegerField(primary_key=True)
    movie_id_tmdb = models.IntegerField()
    movie_title = models.CharField(max_length=200)
