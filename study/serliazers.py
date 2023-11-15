from rest_framework import serializers
from study.models import Course, Lesson, Payment, Subscription
from study.validators import LinkValidator
from users.models import User


class LessonSerializer(serializers.ModelSerializer):
    validators = [LinkValidator(link='link')]

    class Meta:
        model = Lesson
        fields = ("id", "title", "description", "author", "id")


class CourseSerializer(serializers.ModelSerializer):
    number_lessons = serializers.SerializerMethodField()
    course_subscription = serializers.SerializerMethodField()
    lesson = LessonSerializer(source="lesson_set", many=True)

    def get_course_subscription(self, obj):
        return Subscription.objects.filter(course=obj, user=self.context['request'].user).exists()

    def get_number_lessons(self, obj):
        return obj.lesson_set.all().count()

    class Meta:
        model = Course
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'


class SubscriptionListSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='email', queryset=User.objects.all())
    course = serializers.SlugRelatedField(slug_field='title', queryset=Course.objects.all())

    class Meta:
        model = Subscription
        fields = ('id', 'user', 'course')