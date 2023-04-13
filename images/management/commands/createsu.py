import os
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Creates a superuser.'

    def handle(self, *args, **options):
        username = os.getenv('DJANGO_ADMIN_USERNAME')
        password = os.getenv('DJANGO_ADMIN_PASSWORD')
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(
                username=username,
                password=password,
            )
        print('Superuser has been created.')
