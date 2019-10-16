from django.core.management.base import BaseCommand, CommandError
from Responses.models import Responses

class Command(BaseCommand):
    help = 'Shows all data from table: Responses'

    def handle(self, *args, **options):
        objects = Responses.objects.all()
        for obj in objects:
            self.stdout.write('Rating: user: %s, movie: %s, rating: %s' % (
                obj.user_id, obj.movie_id, obj.user_rate))
