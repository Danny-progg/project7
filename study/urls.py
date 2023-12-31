from django.urls import path

from study.apps import StudyConfig
from rest_framework.routers import DefaultRouter

from study.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView, PaymentListAPIView, SubscriptionCreateAPIView, SubscriptionListAPIView, \
    SubscriptionDestroyAPIView

app_name = StudyConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-get'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson-update'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson-delete'),

    path('payments/', PaymentListAPIView.as_view(), name='payment-list'),

    path('subscriptions/create/', SubscriptionCreateAPIView.as_view(), name='subscription-create'),
    path('subscriptions/', SubscriptionListAPIView.as_view(), name='subscription-list'),
    path('subscriptions/<int:pk>/delete/', SubscriptionDestroyAPIView.as_view(), name='subscription-delete'),
] + router.urls