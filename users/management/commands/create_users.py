from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email="tiunovaelena31@gmail.com",
            is_active=True,
        )
        user.set_password("qwe123rty456")
        user.save()
        self.stdout.write(
            self.style.SUCCESS(f"Created user {user.email}")
        )