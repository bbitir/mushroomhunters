from django.forms import ModelForm

from nodes.models import Comment

class CommentCreationForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('body' , 'vote')
