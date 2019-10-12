from django.core.management.base import BaseCommand, CommandError
from Movies.models import Movies

class Command(BaseCommand):
    help = 'Shows all data from table: Movies'

    def handle(self, *args, **options):
        movies = Movies.objects.all()
        for movie in movies:
            self.stdout.write('Movie: "%s"' % movie.movie_title)
