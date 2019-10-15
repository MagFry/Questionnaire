from django.core.management.base import BaseCommand, CommandError
from Users.models import Users

class Command(BaseCommand):
    help = 'Shows all data from table: Users'

    def handle(self, *args, **options):
        users = Users.objects.all()
        for user in users:
            self.stdout.write('Deleting user: "%s"' % user.user_name)
            user.delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted all users from db'))
