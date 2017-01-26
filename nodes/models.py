from django.db import models
from django.conf import settings
from django.utils.encoding import smart_text

class Pile(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return smart_text(self.name)

class Category(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return smart_text(self.name)

class Node(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=255)
    scientific_name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, blank=False, null=True)
    coordinates = models.CharField(max_length=255)
    surface = models.CharField(max_length=255, blank=True, null=True)
    colour = models.CharField(max_length=255, blank=True, null=True)
    pile = models.ForeignKey(Pile, blank=True, null=True)
    aroma = models.CharField('tat', max_length=255, blank=True, null=True)
    season = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    warning = models.TextField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    def __str__(self):
        return smart_text(self.name)

    @models.permalink
    def get_absolute_url(self):
        return('node_detail', (self.id,))


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
