from django.shortcuts import render, get_object_or_404
from nodes.models import Node


def index(request):
    return render(
        request,
        'index.html',
        {
            'nodes': Node.objects.all(),
        }
    )

def detail(request, id):
    return render(
        request,
        'node.html',{
            'node': get_object_or_404(Node, id=id)
        }
    )

##def review(request):
##    return render(
##        request,
##        'review.html',
##        {
##            '': Comment.objects.all(),
##        }
##    )
