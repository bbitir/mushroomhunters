from django.shortcuts import render
from nodes.models import Node

def index(request):
    return render(
        request,
        'index.html',
        {
            'nodes': Node.objects.all(),
        }
    )
