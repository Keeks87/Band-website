from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required

@login_required
def post_detail(request, pk):
    """
    Display details of a single blog post and handle adding comments.

    If the request method is GET, render the `post_detail.html` template with the
    specified post and all comments associated with it. If the request method is
    POST, validate the submitted comment form and add a new comment to the post.

    If the form is not valid, re-render the `post_detail.html` template with the
    specified post, comments, and invalid form. If the form is valid, redirect to
    the `post_detail` view for the specified post.

    Requires login. Redirects to the login page if the user is not authenticated.
    """
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'form': form})
