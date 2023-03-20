from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    """
    A form for creating a new comment on a blog post.

    The form contains a single field for the body of the comment.
    """
    class Meta:
        model = Comment
        fields = ('body',)
