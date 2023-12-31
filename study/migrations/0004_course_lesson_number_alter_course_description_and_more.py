# Generated by Django 4.2.7 on 2023-11-08 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0003_lesson_alter_course_description_alter_course_preview'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='lesson_number',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='study.lesson', verbose_name='количество уроков'),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='title',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='название'),
        ),
    ]
