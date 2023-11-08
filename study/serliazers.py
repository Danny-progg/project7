from rest_framework import serializers

from study.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ("title", "description")


class CourseSerializer(serializers.ModelSerializer):
    number_lessons = serializers.SerializerMethodField()

    lesson = LessonSerializer(source="lesson_set", many=True)

    def get_number_lessons(self, obj):
        return obj.lesson_set.all().count()

    class Meta:
        model = Course
        fields = '__all__'

