from django.core.management.base import BaseCommand
from django.utils import timezone
from study.models import Payment, Lesson, Course
from users.models import User
from decimal import Decimal
import random


class Command(BaseCommand):
    help = 'Create random payments'

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        courses = Course.objects.all()
        lessons = Lesson.objects.all()

        for user in users:
            payment = Payment(
                user=user,
                data_pay=timezone.now(),
                pay_course=random.choice(courses) if courses else None,
                pay_lesson=random.choice(lessons) if lessons else None,
                amount=Decimal(random.uniform(10, 2000)),
                payment_method=random.choice([Payment.CASH, Payment.BANK_TRANSFER])
            )
            payment.save()