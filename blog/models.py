from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    #author = models.CharField(max_length=250)
    #title = models.CharField(max_length=250)
    #text = models.CharField(max_length=250)
    #
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        'blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=72)
    text = models.TextField(max_length=250)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
