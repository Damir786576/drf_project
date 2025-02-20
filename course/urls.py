from rest_framework.routers import SimpleRouter

from course.views import CourseViewSet
from course.apps import CourseConfig

app_name = CourseConfig.name

routers = SimpleRouter()
routers.register("", CourseViewSet)

urlpatterns = []

urlpatterns += routers.urls

