from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Post, Comment
from django.contrib.auth import get_user_model, views, models, login
from django.views.generic import CreateView 
from .form import PostForm, UserForm, CommentForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.core.paginator import Paginator
from django.contrib import messages

#api & jwt 관련
from django.core import serializers
from rest_framework.decorators import api_view, permission_classes, authentication_classes  #데코레이터는 간단히 말하면 전처리.
from rest_framework.permissions import IsAuthenticated  #로그인 여부를 확인할 때 사용한다.
from rest_framework_jwt.authentication import JSONWebTokenAuthentication  #JWT 인증을 확인하기 위해 사용.


@api_view(['GET'])  #def posts(request) 실행 전에 먼저 실행됨. GET 요청인지 확인 후 아니라면 error 반환
@permission_classes((IsAuthenticated, ))    #권한을 체크함. 여기서는 로그인 했는지 여부만 확인.
@authentication_classes((JSONWebTokenAuthentication,))  #jwt 토큰을 확인.
def posts(request):
    posts = Post.objects.filter(
        published_date__isnull=False).order_by('-created_date') 
    #json 형태로 직렬화(serializeration)
    post_list = serializers.serialize('json', posts)
    return HttpResponse(post_list, content_type="text/json-comment-filtered")

#회원가입. 
def signup(request):
    if request.method == "POST": #1
        #유저가 입력한 비밀번호와 비밀번호 확인이 동일하다면
        if request.POST["password1"] == request.POST["password2"]:
            user = models.User.objects.create_user(
                username = request.POST["username"], 
                password = request.POST["password1"])
            messages.info(request, '회원가입을 환영합니다! 로그인 후 글을 남겨보세요.')
            return redirect(post_list)
        else:
            messages.info(request, '입력한 비밀번호를 확인하세요')
        return render(request, 'blog/signup.html')
    return render(request, 'blog/signup.html') #4

def post_list(request):
    posts = Post.objects.filter(published_date__isnull=False).order_by('-created_date') 
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    pageposts = paginator.get_page(page)
    return render(request, 'blog/post_list.html', {'posts':posts,'pageposts':pageposts})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    #댓글 작성 request가 들어오면
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect(post_detail, pk=pk)
    #댓글 작성 request가 아니고, post_list에서 게시물 클릭 시
    else:
        #댓글 작성 form을 불러온다
        form = CommentForm()
    
    context = {
        'post': post,
        'form' : form
    } 
    return render(request, 'blog/post_detail.html', context)

@login_required
def comment_remove(request, pk, cpk):
    post = get_object_or_404(Post, pk=pk)
    comment = Comment.objects.get(pk=cpk)
    if not comment.author == request.user:
        return redirect(post_detail, pk=pk)
    else:
        comment.delete()
        return redirect(post_detail, pk=pk)

@login_required
def post_add(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = models.User.objects.get(username=request.user.get_username())  
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
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect(post_detail, pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

