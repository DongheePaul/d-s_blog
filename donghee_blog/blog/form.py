from django import forms
from .models import Post
from django.contrib.auth.models import User #1
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [ 'title', 'mainphoto', 'content',]

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username',]