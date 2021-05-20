from django.http import JsonResponse
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, CreateAPIView
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from main.models import *
from main.serializers import TopicSerializer


class TopicList(generics.GenericAPIView, mixins.ListModelMixin,):
    # permission_classes = [IsAdminUser]
    # renderer_classes = [JSONRenderer]
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()

    tags = list(queryset.values_list('Tag', flat=True))
    print(tags[0])

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class TopicDetail(generics.GenericAPIView, mixins.RetrieveModelMixin,):
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class TopicCreate(generics.CreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class TopicUpdate(generics.RetrieveUpdateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class TopicDelete(generics.RetrieveDestroyAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

