from django.contrib import admin
from nodes.models import (Node, Pile, Category, Comment)

admin.site.register(Node)
admin.site.register(Pile)
admin.site.register(Category)
admin.site.register(Comment)
