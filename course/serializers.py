from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from course.validators import validate_youtube_link

from course.models import Course, Lessons, Subscription


class LessonDetailSerializer(ModelSerializer):
    count_lessons_with_same_course = SerializerMethodField()

    def get_count_lessons_with_same_course(self, lesson):
        return Lessons.objects.filter(course=lesson.course).count()

    class Meta:
        model = Lessons
        fields = ("name", "course", "count_lessons_with_same_course")


class LessonsSerializer(ModelSerializer):
    name = serializers.URLField(validators=[validate_youtube_link])

    class Meta:
        model = Lessons
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonsSerializer(many=True, read_only=True)
    count_lessons = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['id', 'title', 'preview', 'description', 'lessons', 'count_lessons']

    def get_count_lessons(self, course):
        return course.lessons.count()


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['user', 'course']
        read_only_fields = ['user', 'course']
