from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Post
from django.contrib.auth import get_user_model, views, models, login
from django.views.generic import CreateView 
from .form import PostForm, UserForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import auth

#회원가입. 
def signup(request):
    if request.method == "POST": #1
        #유저가 입력한 비밀번호와 비밀번호 확인이 동일하다면
        if request.POST["password1"] == request.POST["password2"]:
            user = models.User.objects.create_user(
                username = request.POST["username"], 
                password = request.POST["password1"])
            return redirect(post_list)
        return render(request, 'blog/signup.html')
    return render(request, 'blog/signup.html') #4

def post_list(request):
    posts = Post.objects.filter(published_date__isnull=False).order_by('-created_date')  # 수정된 부분
    context = {
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context)

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post': post
    } 
    return render(request, 'blog/post_detail.html', context)

@login_required
def post_add(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            # 기본키를 전달한 post_detail 뷰를 redirect 함수에 전달.
            return redirect(post_list)
    else:
        form = PostForm()
        return render(request, 'blog/post_add.html', {'form': form})

@login_required
def post_delete(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        post.delete()
        return render(request, 'blog/post_delete.html')

    elif request.method == 'GET':
        return HttpResponse('잘못된 접근 입니다.')

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect(post_detail, pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})