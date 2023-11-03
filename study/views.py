from rest_framework import viewsets

from study.models import Course
from study.serliazers import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
