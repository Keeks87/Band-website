from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    """
    A model representing a blog post.

    Attributes:
        title (str): The title of the post.
        body (str): The body of the post.
        date (datetime): The date and time when the post was created.
    """

    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()
    def __str__(self):
        return self.title

class Comment(models.Model):
    """
    A model representing a comment on a blog post.

    Attributes:
        post (Post): The post that the comment is associated with.
        author (User): The user who wrote the comment.
        body (str): The body of the comment.
        created_on (datetime): The date and time when the comment was created.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.author)
