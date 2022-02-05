from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Creates an admin user non-interactively if it doesn't exist"

    def add_arguments(self, parser):
        parser.add_argument('--superuser', help="If user is a superuser")
        parser.add_argument('--username', help="Set username")
        parser.add_argument('--email', help="Set email")
        parser.add_argument('--password', help="Set password")

    def handle(self, *args, **options):
        User = get_user_model()
        if options['superuser'] is not None and options['username'] is not None:
            if not User.objects.filter(username=options['username']).exists():
                User.objects.create_superuser(username=options['username'],
                                          email=options['email'],
                                          password=options['password'])
                print("Superuser created!")
                
        elif options['username'] is not None:
            if not User.objects.filter(username=options['username']).exists():
                User.objects.create_user(username=options['username'],
                                          email=options['email'],
                                          password=options['password'])
                print("User created!")