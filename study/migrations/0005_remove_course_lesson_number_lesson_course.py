# Generated by Django 4.2.7 on 2023-11-08 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0004_course_lesson_number_alter_course_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='lesson_number',
        ),
        migrations.AddField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='study.course', verbose_name='курс'),
        ),
    ]