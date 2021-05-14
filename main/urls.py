from django.urls import path
from . import views
from .models import Topic
from .serializers import TopicSerializer
from .views import TopicDetail, TopicList


urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('topic-list/', TopicList.as_view(queryset=Topic.objects.all(), serializer_class=TopicSerializer), name='topic-list'),
    path('topic-detail/<str:pk>/', TopicDetail.as_view(queryset=Topic.objects.all(), serializer_class=TopicSerializer), name='topic-detail'),
    path('topic-create/', views.topicCreate, name='topic-create'),
    path('topic-update/<str:pk>/', views.topicUpdate, name='topic-update'),
    path('topic-delete/<str:pk>/', views.topicDelete, name='topic-delete'),
]
