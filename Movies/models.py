from django.db import models

# Create your models here.


class Movies(models.Model):
    movie_id = models.IntegerField(primary_key=True)
    movie_id_tmdb = models.IntegerField()
    movie_title = models.CharField(max_length=200)
    # comma separated list of genres, e.g. Comedy,Horror
    movie_genres = models.CharField(max_length=800)
    # a string with movie description
    overview = models.CharField(max_length=3000)
    # path to local image file, e.g. "adw6Lq9FiC9zjYEpOqfq03ituwp.jpg"
    # those files will be put to media/ directory
    poster_path = models.CharField(max_length=500)
    # e.g. "1999-10-15"
    release_date = models.CharField(max_length=10)
    # e.g. 8.4
    vote_average = models.FloatField()


    def __str__(self):
        return self.movie_title


    # returns an array of strings, e.g. ['Comedy', 'Horror']
    def get_genres_as_array(self):
        return self.movie_genres.split(',')


    # returns True if this movie genres contains specific_genre
    def is_of_specific_genre(self, specific_genre):
        genres_array = self.get_genres_as_array()
        return specific_genre in genres_array


    # returns True if this movie genres exclude all the genres from specific_genres_arr
    def excludes_specific_genres(self, specific_genres_arr):
        genres_array = self.get_genres_as_array()
        for genre in specific_genres_arr:
            if genre in genres_array:
                return False
        return True

    # return an array of movies which are of specific genre, but also
    # their genres are not in excluded_genres_arr
    # (this method will be used to produce different views, e.g.
    # a view with movies that are romance, but not comedy and not horror)
    def get_movies_by_genre(self, genre, excluded_genres_arr):
        movies_in_db = Movies.objects.all()
        movies_to_be_returned = []
        for movie in movies_in_db:
            if movie.is_of_specific_genre(genre) and movie.excludes_specific_genres(excluded_genres_arr):
                movies_to_be_returned.append(movie)
        return movies_to_be_returned
