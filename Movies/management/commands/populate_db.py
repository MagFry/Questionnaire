from django.core.management.base import BaseCommand, CommandError
from Movies.models import Movies

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

                self.stdout.write('Adding movie: "%s;%s;%s"' % (id,id_tmdb,title))

                movie_l = Movies.objects.create(movie_id=id, movie_id_tmdb=id_tmdb, movie_title=title)
            self.stdout.write(self.style.SUCCESS('Successfully added all movies to db'))
