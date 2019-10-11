from django.core.management.base import BaseCommand, CommandError
from Movies.models import Movies

class Command(BaseCommand):
    help = 'Deletes all data from table: Movies'

    def handle(self, *args, **options):
        movies = Movies.objects.all()
        for movie in movies:
            self.stdout.write('Deleting movie: "%s"' % movie.movie_title)
            movie.delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted all movies from db'))
