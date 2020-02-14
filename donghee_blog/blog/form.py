from django import forms
from .models import Post, Comment
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

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

        widgets={
            "text":forms.Textarea(attrs={'placeholder':'배려와 매너가 밝은 커뮤니티를 만듭니다.','class':'form-control','rows':5}),
        }
        labels={
            "text":""
        }