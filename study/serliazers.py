from rest_framework import serializers

from study.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ("id", "title", "description", "course")


class CourseSerializer(serializers.ModelSerializer):
    number_lessons = serializers.SerializerMethodField()
    lesson = LessonSerializer(many=True, read_only=True)

    def get_number_lessons(self, obj):
        return obj.lesson_set.all().count()

    class Meta:
        model = Course
        fields = '__all__'

