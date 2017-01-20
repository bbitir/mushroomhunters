from django.db import models
from django.conf import settings
from django.utils.encoding import smart_text

class Node(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=255)
    scientific_name = models.CharField(max_length=255)
    coordinates = models.CharField(max_length=255)
    description = models.TextField(max_length=500, blank=True, null=True)
    def __str__(self):
        return smart_text(self.name)

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    node = models.ForeignKey(Node)
    body = models.TextField(max_length=500, blank=False, null=True)
    vote = models.IntegerField(
        choices=(
            (1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
        )
    )
    def __str__(self):
        return smart_text(self.body)
