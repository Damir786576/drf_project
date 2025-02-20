from rest_framework.serializers import ModelSerializer

from lessons.models import Lessons


class LessonsSerializer(ModelSerializer):
    class Meta:
        model = Lessons
        fields = "__all__"


