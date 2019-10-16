from django.core.management.base import BaseCommand, CommandError
from Movies.models import Movies
import Movies.tmdb_api_client as tmdb_api_client
import os

# Why this file exists?
# https://eli.thegreenplace.net/2014/02/15/programmatically-populating-a-django-database
# https://docs.djangoproject.com/en/2.2/howto/custom-management-commands/

class Command(BaseCommand):
    help = 'Adds data to table: Movies from csv file and from TMDB API'

    def handle(self, *args, **options):
        movies = Movies.objects.all()
        if len(movies) != 0:
            self.stdout.write('Skipping populating the Movies table')
        else:
            self.stdout.write('Populating the Movies table')

            file_path = 'Data/movies.csv'
            with open(file_path, "r") as ins:
                ids = []
                ids_tmdb = []
                title = []
                for line in ins:
                    split_line = line.split('\t')
                    ids.append(split_line[0])
                    ids_tmdb.append(split_line[1])
                    title.append(split_line[2])

            list = []
            #keys = ["file_id", "file_id_tmdb", "title"]
            #temp_dict = {}
            array_lenght = len(ids)

            for i in range(array_lenght):
                temp_dict = {"file_id":int(ids[i]), "file_id_tmdb":int (ids_tmdb[i]),  "title": title[i] }
                list.append(temp_dict)


            for item in list:
                id = item.get('file_id')
                id_tmdb = item.get('file_id_tmdb')
                title = item.get('title').rstrip()

                # get additional information using TMDB API
                json = tmdb_api_client.get_movie_json(id_tmdb, tmdb_api_client.api_key_v3)
                genres = tmdb_api_client.get_movie_genres_comma_separated(json)

                self.stdout.write('Adding movie: "%s;%s;%s"' % (id,id_tmdb,title))
                movie_l = Movies.objects.create(
                    movie_id=id, movie_id_tmdb=id_tmdb, movie_title=title,
                    movie_genres=genres, overview=json['overview'],
                    poster_path=json['poster_path'], release_date=json['release_date'],
                    vote_average=float(json['vote_average']))
                self.stdout.write('Downloading poster image')
                tmdb_api_client.download_poster(json)

                if os.environ.get('PIIS_TEST') == 'true':
                    if len(Movies.objects.all()) >= 10:
                        self.stdout.write('PIIS_TEST set to true, no more movies will be added')
                        break

            self.stdout.write(self.style.SUCCESS('Successfully added all movies to db'))
