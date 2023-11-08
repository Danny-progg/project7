from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Lesson(models.Model):
    title = models.CharField(max_length=150, verbose_name='название', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)
    preview = models.ImageField(upload_to='images/', verbose_name='изображение', **NULLABLE)
    link_video = models.CharField(max_length=150, verbose_name='ссылка на видео', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name='название', **NULLABLE)
    description = models.TextField(verbose_name='описание', **NULLABLE)
    preview = models.ImageField(upload_to='images/', verbose_name='изображение', **NULLABLE)
    lesson_number = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='количество уроков', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'