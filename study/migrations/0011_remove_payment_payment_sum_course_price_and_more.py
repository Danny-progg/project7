# Generated by Django 4.2.7 on 2023-11-15 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0010_alter_payment_options_remove_lesson_link_video_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='payment_sum',
        ),
        migrations.AddField(
            model_name='course',
            name='price',
            field=models.PositiveIntegerField(blank=True, default=1000, null=True, verbose_name='Стоимость курса'),
        ),
        migrations.AddField(
            model_name='payment',
            name='is_successful',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Статус платежа'),
        ),
        migrations.AddField(
            model_name='payment',
            name='session',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Сессия для оплаты'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_method',
            field=models.CharField(blank=True, choices=[('1', 'Наличные'), ('2', 'Безнал')], max_length=1, null=True, verbose_name='Метод платежа'),
        ),
    ]