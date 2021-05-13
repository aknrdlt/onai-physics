from django.urls import path
from . import views
from .views import TopicDetail, TopicList

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('topic-list/', TopicList.as_view(), name='topic-list'),
    path('topic-detail/<str:pk>/', TopicDetail.as_view(), name='topic-detail'),
    path('topic-create/', views.topicCreate, name='topic-create'),
    path('topic-update/<str:pk>/', views.topicUpdate, name='topic-update'),
    path('topic-delete/<str:pk>/', views.topicDelete, name='topic-delete'),
]
