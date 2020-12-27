from django import forms
from .models import Post, Comment
#from django.db import models


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')


class CommentForm(forms.ModelForm):
    class Meta:
        #text = forms.CharField(max_length=250)
        #author = forms.CharField(max_length=250)
        model = Comment
        fields = ['text', ]
