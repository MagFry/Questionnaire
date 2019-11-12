from django.test import TestCase
from Movies.models import Movies
from Responses.models import Responses
from Users.models import Users
import Movies.tmdb_api_client as tmdb_api_client
import os.path

# https://docs.djangoproject.com/en/2.2/topics/testing/overview/
# https://docs.djangoproject.com/en/2.2/intro/tutorial05/

class TmdbApiClient(TestCase):
    def test_get_movie_json(self):
        """Api Client can get info about a movie as JSON"""
        json = tmdb_api_client.get_movie_json(551, tmdb_api_client.api_key_v3)
        self.assertEqual(json['genres'], [{"id":28,"name":"Action"},{"id":12,"name":"Adventure"},{"id":18,"name":"Drama"}])
        self.assertEqual(json['adult'], False)
        self.assertEqual(json['release_date'], "1972-12-01")

    def test_get_movie_genres(self):
        """Api Client can get movie genres as an array"""
        json = {}
        json['genres'] = [{'id': 18, 'name': 'Drama'},{'id': 19, 'name': 'sth'}]
        genres = tmdb_api_client.get_movie_genres(json)
        self.assertEqual(genres, ['Drama', 'sth'])

    def test_get_movie_genres_integration(self):
        """Api Client can get movie genres as an array"""
        json = tmdb_api_client.get_movie_json(551, tmdb_api_client.api_key_v3)
        genres = tmdb_api_client.get_movie_genres(json)
        self.assertEqual(genres, ['Action', 'Adventure', 'Drama'])

    def test_get_movie_genres_comma_separated(self):
        """Api Client can get movie genres as comma separated string"""
        json = {}
        json['genres'] = [{"id":28,"name":"Action"},{"id":12,"name":"Adventure"},{"id":18,"name":"Drama"}]
        genres = tmdb_api_client.get_movie_genres_comma_separated(json)
        self.assertEqual(genres, 'Action,Adventure,Drama')

    def test_get_movie_genres_comma_separated_integration(self):
        """Api Client can get movie genres as comma separated string"""
        json = tmdb_api_client.get_movie_json(551, tmdb_api_client.api_key_v3)
        genres = tmdb_api_client.get_movie_genres_comma_separated(json)
        self.assertEqual(genres, 'Action,Adventure,Drama')

    def test_download_poster(self):
        """Api Client can download poster image"""
        poster_path = 'adw6Lq9FiC9zjYEpOqfq03ituwp.jpg'
        test_images_dir = 'test/media'
        # clean before test
        if os.path.isfile(test_images_dir+'/'+poster_path):
            os.remove(test_images_dir+'/'+poster_path)
        json = {}
        json['poster_path'] = poster_path
        tmdb_api_client.download_poster(json, test_images_dir)
        self.assertEqual(os.path.isfile(test_images_dir+'/'+poster_path), True)
        # clean after test
        if os.path.isfile(test_images_dir+'/'+poster_path):
            os.remove(test_images_dir+'/'+poster_path)

    def test_get_polish_movie_details(self):
        """Api Client can get polish details about a movie"""
        details = tmdb_api_client.get_polish_movie_details(551, tmdb_api_client.api_key_v3)
        self.assertEqual(details['title'], 'Tragedia Posejdona')
        self.assertTrue('Noc sylwestrowa. Grupa pasażerów walczy o przeżycie' in details['overview'])

class MoviesTestCase(TestCase):
    def setUp(self):
        m1 = Movies.objects.create(movie_id=1, movie_id_tmdb=1, movie_title="title1",
         movie_genres="Comedy,Horror", overview="movie1", poster_path="Data/movie1.jpg",
         release_date="1999-10-15", vote_average=5.0)
        m2 = Movies.objects.create(movie_id=2, movie_id_tmdb=2, movie_title="title2",
         movie_genres="Horror", overview="movie2", poster_path="Data/movie2.jpg",
         release_date="1999-10-15", vote_average=5.0)
        m3 = Movies.objects.create(movie_id=3, movie_id_tmdb=3, movie_title="title3",
         movie_genres="Thriller", overview="movie3", poster_path="Data/movie3.jpg",
         release_date="1999-10-15", vote_average=5.0)
        u1 = Users.objects.create(user_id=1, user_name="user1")
        u37 = Users.objects.create(user_id=37, user_name="user37")
        Responses.objects.create(respond_id=666, movie_id=m2, user_id=u37,
         user_rate=3)
        Responses.objects.create(respond_id=667, movie_id=m3, user_id=u37,
         user_rate=0)

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
        self.assertEqual(Movies.get_movies_by_genre('Horror', []), [movie1,movie2])
        self.assertEqual(Movies.get_movies_by_genre('sth1', []), [])
        self.assertEqual(Movies.get_movies_by_genre('Horror', ['sth1']), [movie1,movie2])
        self.assertEqual(Movies.get_movies_by_genre('Thriller', ['Horror','Comedy']), [movie3])
        self.assertEqual(Movies.get_movies_by_genre('Thriller', []), [movie3])

    def test_movie_get_movies_by_ids(self):
        movie1 = Movies.objects.get(movie_title="title1")
        movie2 = Movies.objects.get(movie_title="title2")
        movie3 = Movies.objects.get(movie_title="title3")
        self.assertEqual(Movies.get_movies_by_ids([]), [])
        self.assertEqual(Movies.get_movies_by_ids([1]), [movie1])
        self.assertEqual(Movies.get_movies_by_ids([1,3]), [movie1,movie3])

    def test_movie_get_unassessed_movies(self):
        responses_by_user0 = []
        self.assertEqual(Movies.get_unassessed_movies(99, responses_by_user0, 3), [1,2,3])

        response1 = Responses.objects.get(respond_id=666)
        response2 = Responses.objects.get(respond_id=667)
        responses_by_user37 = [response1,response2]
        self.assertEqual(Movies.get_unassessed_movies(37, responses_by_user37, 3), [1,3])
