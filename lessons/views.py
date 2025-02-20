from rest_framework.generics import (
    CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
)
from rest_framework.viewsets import ModelViewSet

from lessons.models import Lessons
from lessons.serializers import LessonsSerializer


class LessonsViewSet(ModelViewSet):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer


class LessonsCreateApiView(CreateAPIView):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer


class LessonsListAPIView(ListAPIView):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer


class LessonsRetrieveAPIView(RetrieveAPIView):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer


class LessonsUpdateAPIView(UpdateAPIView):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer


class LessonsDestroyAPIView(DestroyAPIView):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer
