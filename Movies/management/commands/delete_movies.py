from django.core.management.base import BaseCommand, CommandError
from Movies.models import Movies
import os.path

class Command(BaseCommand):
    help = 'Deletes all data from table: Movies'

    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            '--media-dir',
            dest = "mediadir",
            help='Directory for media files',
        )

    def handle(self, *args, **options):
        media_dir = 'media'
        if options['mediadir'] != None:
            media_dir = options['mediadir']

        movies = Movies.objects.all()
        for movie in movies:
            self.stdout.write('Deleting movie: "%s"' % movie.movie_title)
            # remove poster image
            poster_path = media_dir + "/" + movie.poster_path
            self.stdout.write('Deleting poster: "%s"' % poster_path)
            if os.path.isfile(poster_path):
                os.remove(poster_path)
            # delete movie from db
            movie.delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted all movies from db'))
