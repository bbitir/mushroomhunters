from django.db import models
from django.conf import settings
from django.utils.encoding import smart_text

class Node(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=255)
    scientific_name = models.CharField(max_length=255)
    coordinates = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return smart_text(self.name)
