from django.test import TestCase
from Movies.models import Movies

# https://docs.djangoproject.com/en/2.2/topics/testing/overview/
# https://docs.djangoproject.com/en/2.2/intro/tutorial05/

class MoviesTestCase(TestCase):
    def setUp(self):
        Movies.objects.create(movie_id=1, movie_id_tmdb=1, movie_title="title1", movie_genres="Comedy,Horror")
        Movies.objects.create(movie_id=2, movie_id_tmdb=2, movie_title="title2", movie_genres="Horror")
        Movies.objects.create(movie_id=3, movie_id_tmdb=3, movie_title="title3", movie_genres="Thriller")

    def test_movie_get_genres_as_array(self):
        """Movie can return its genres as an array"""
        movie1 = Movies.objects.get(movie_title="title1")
        movie2 = Movies.objects.get(movie_title="title2")
        self.assertEqual(movie1.get_genres_as_array(), ['Comedy', 'Horror'])
        self.assertEqual(movie2.get_genres_as_array(), ['Horror'])

    def test_movie_is_of_specific_genre(self):
        movie1 = Movies.objects.get(movie_title="title1")
        self.assertEqual(movie1.is_of_specific_genre('Comedy'), True)
        self.assertEqual(movie1.is_of_specific_genre('Horror'), True)
        self.assertEqual(movie1.is_of_specific_genre('NotExisting'), False)

    def test_movie_excludes_specific_genres(self):
        movie1 = Movies.objects.get(movie_title="title1")
        self.assertEqual(movie1.excludes_specific_genres(['Comedy']), False)
        self.assertEqual(movie1.excludes_specific_genres(['Horror']), False)
        self.assertEqual(movie1.excludes_specific_genres(['Comedy','Horror']), False)
        self.assertEqual(movie1.excludes_specific_genres(['Comedy','Horror','sth1']), False)
        self.assertEqual(movie1.excludes_specific_genres(['Comedy','sth1']), False)
        self.assertEqual(movie1.excludes_specific_genres(['sth1']), True)

    def test_movie_get_movies_by_genre(self):
        movie1 = Movies.objects.get(movie_title="title1")
        movie2 = Movies.objects.get(movie_title="title2")
        movie3 = Movies.objects.get(movie_title="title3")
        self.assertEqual(movie1.get_movies_by_genre('Horror', []), [movie1,movie2])
        self.assertEqual(movie1.get_movies_by_genre('sth1', []), [])
        self.assertEqual(movie1.get_movies_by_genre('Horror', ['sth1']), [movie1,movie2])
        self.assertEqual(movie1.get_movies_by_genre('Thriller', ['Horror','Comedy']), [movie3])
        self.assertEqual(movie1.get_movies_by_genre('Thriller', []), [movie3])
