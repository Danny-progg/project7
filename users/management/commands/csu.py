from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):

        user = User.objects.create(
            email='daniilmurzin333@gmail.com',
            first_name='Admin',
            last_name='flarpz',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('852799')
        user.save()