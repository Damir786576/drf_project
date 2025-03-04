from django.urls import path
from rest_framework.routers import SimpleRouter

from course.views import CourseViewSet, LessonsListAPIView, LessonsCreateApiView, LessonsRetrieveAPIView, \
    LessonsUpdateAPIView, LessonsDestroyAPIView, SubscriptionView
from course.apps import CourseConfig

app_name = CourseConfig.name

routers = SimpleRouter()
routers.register("", CourseViewSet)

urlpatterns = [
    path("lessons/", LessonsListAPIView.as_view(), name="lessons-list"),
    path("lessons/create/", LessonsCreateApiView.as_view(), name="lessons-create"),
    path("lessons/<int:pk>/", LessonsRetrieveAPIView.as_view(), name="lessons-detail"),
    path("lessons/<int:pk>/update/", LessonsUpdateAPIView.as_view(), name="lessons-update"),
    path("lessons/<int:pk>/delete/", LessonsDestroyAPIView.as_view(), name="lessons-delete"),
    path('subscribe/', SubscriptionView.as_view(), name='subscribe'),
]

urlpatterns += routers.urls
