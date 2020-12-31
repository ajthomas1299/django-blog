from django import forms
from django.contrib.auth.models import User
from .models import Post, Comment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
#from crispy_forms.bootstrap import (PrependedText, PrependedAppendedText, FormActions)


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


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('Sign up', 'Sign up', css_class='btn btn-success'))

    class Meta:
        model = User
        fields = ('username', 'email', 'password', )
