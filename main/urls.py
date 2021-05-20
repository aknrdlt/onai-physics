from django.urls import path
from . import views
from .models import Topic
from .serializers import TopicSerializer
from .views import *

urlpatterns = [
    path('topic-list/', TopicList.as_view(), name='topic-list'),
    path('topic-detail/<int:pk>/', TopicDetail.as_view(), name='topic-detail'),
    path('topic-create/', TopicCreate.as_view(), name='topic-create'),
    path('topic-update/<int:pk>/',  TopicUpdate.as_view(), name='topic-update'),
    path('topic-delete/<int:pk>/', TopicDelete.as_view(), name='topic-delete'),
]
