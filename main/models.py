from django.db import models

# Create your models here.


class Topic(models.Model):
    name = models.CharField(max_length=200, null=True)
    link = models.CharField(max_length=400, null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return str(self.name)
