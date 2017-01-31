from django.shortcuts import render, get_object_or_404 , redirect
from nodes.models import Node
from django.contrib import messages

from nodes.forms import CommentCreationForm

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
def new_comment(request, node_id):
    node = get_object_or_404 (Node, id=node_id)
    form = CommentCreationForm()

    if request.method == "POST" :
        form = CommentCreationForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.instance.node = node
            form.save()
            messages.info(
                request,
                'Yorumunuz eklendi.'
            )
            return redirect(node.get_absolute_url())
    return render(
        request,
        'new_comment.html' ,
        {
            'node' : node,
            'form' : form,

        }
    )
