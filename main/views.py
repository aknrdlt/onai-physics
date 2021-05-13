from django.http import JsonResponse
from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from main.models import *
from main.serializers import TopicSerializer


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Topics': '/topic-list/',
        'Topic': '/topic/<str:pk>',
        'Create': '/topic-create/',
        'Update': '/topic-update/<str:pk>',
        'Delete': '/topic-delete/'
    }
    return Response(api_urls)


class TopicList(generics.ListCreateAPIView):
    topics = Topic.objects.all()
    serializer = TopicSerializer(topics, many=True)
    pass


class TopicDetail(generics.RetrieveDestroyAPIView):
    pass


@api_view(['POST'])
def topicCreate(request):
    serializer = TopicSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def topicUpdate(request, pk):
    try:
        topic = Topic.objects.get(id=pk)
    except Topic.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TopicSerializer(instance=topic, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def topicDelete(request, pk):
    try:
        topic = Topic.objects.get(id=pk)
    except Topic.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    topic.delete()
    return Response('Topic successfully deleted!')