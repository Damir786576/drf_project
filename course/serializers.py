from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from course.models import Course, Lessons


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class LessonDetailSerializer(ModelSerializer):
    count_lessons_with_same_course = SerializerMethodField()

    def get_count_lessons_with_same_course(self, lesson):
        return Lessons.objects.filter(course=lesson.course).count()

    class Meta:
        model = Lessons
        fields = ("name", "course", "count_lessons_with_same_course")


class LessonsSerializer(ModelSerializer):
    class Meta:
        model = Lessons
        fields = "__all__"
