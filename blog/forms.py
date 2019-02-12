from django.forms import ModelForm
from blog.models import Post
from django import forms



class PostForm(ModelForm):

    class Meta:
        model = Post
        fields='__all__'
