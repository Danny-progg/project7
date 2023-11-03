from study.apps import StudyConfig
from rest_framework.routers import DefaultRouter

from study.views import CourseViewSet

app_name = StudyConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [

] + router.urls