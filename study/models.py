from django.db import models

from config import settings
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='название', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)
    preview = models.ImageField(upload_to='images/', verbose_name='изображение', **NULLABLE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='автор', **NULLABLE)
    price = models.PositiveIntegerField(default=1000, verbose_name='Стоимость курса', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=150, verbose_name='название', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)
    preview = models.ImageField(upload_to='images/', verbose_name='изображение', **NULLABLE)
    link = models.URLField(verbose_name='Ссылка на видео', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', **NULLABLE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='автор', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_payments', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_payments', **NULLABLE)
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата платежа', **NULLABLE)
    payment_method = models.CharField(max_length=1, choices=[('1', 'Наличные'), ('2', 'Безнал')], verbose_name='Метод платежа', **NULLABLE)
    is_successful = models.BooleanField(default=False, verbose_name='Статус платежа', **NULLABLE)
    session = models.CharField(max_length=150, verbose_name='Сессия для оплаты', **NULLABLE)

    def __str__(self):
        return f"{self.user}: {self.course} - {self.payment_date}"

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
        ordering = ('-payment_date',)


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_subscriptions', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_subscriptions', **NULLABLE)

    def __str__(self):
        return f"{self.user}: {self.course}"

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'