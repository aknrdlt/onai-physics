from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Topic(models.Model):

    class TopicObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    name = models.CharField(max_length=200, null=True)
    link = models.CharField(max_length=400, null=True)
    description = models.TextField(null=True)
    slug = models.SlugField(max_length=250, null=True, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    objects = models.Manager()
    topicObjects = TopicObjects

    def __str__(self):
        return str(self.name)


