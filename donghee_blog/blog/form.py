from django import forms
from .models import Post, Comment
from django.contrib.auth.models import User #1
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import ClearableFileInput

class MyClearableFileInput(ClearableFileInput):
    initial_text = ''
    input_text = '바꿀사진'
    clear_checkbox_label = '삭제'

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [ 'title', 'mainphoto', 'content',]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'15자 이내로 입력 가능합니다.'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'mainphoto' : MyClearableFileInput
        }
        labels = {
            'title': '제목',
            'mainphoto': '사진',
            'content': '내용'
        }
    # 글자수 제한
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__( *args, **kwargs)
        self.fields['title'].widget.attrs['maxlength'] = 15

    def clean(self):
        cleaned_data = super(PostForm, self).clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        if not title and not content:
            raise forms.ValidationError('You have to write something!')

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