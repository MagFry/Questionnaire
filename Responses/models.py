from django.db import models
from Movies.models import Movies
from Users.models import Users

# Create your models here.


class Responses(models.Model):
    respond_id = models.IntegerField(primary_key=True)
    movie_id = models.ForeignKey(Movies, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.respond_id
