from django.http import HttpResponse
from django.shortcuts import render, redirect
from blog.models import Post
from django.contrib.auth import get_user_model


def helloworld(request):
    return HttpResponse('hello world!')

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

def post_add(request):
    return render(request, 'blog/post_add.html')

def post_add(request):
    if request.method == 'POST':
        # User 객체를 생성
        User = get_user_model()  
        # User 객체를 통해 이름이 'donghee' 인 User 객체를 불러와 'author' 변수에 할당
        author = User.objects.get(username='donghee')  
        title = request.POST['title']
        content = request.POST['content']
        posts = Post.objects.create(
            author = author,
            title = title,
            content = content,
        )
        posts.publish()
        # 등록한 글의 기본키를 가져와서 posts_pk 변수에 할당.
        posts_pk = posts.pk
        # 기본키를 전달한 post_detail 뷰를 redirect 함수에 전달.
        return redirect(post_detail, pk=posts_pk)
    elif request.method == 'GET':
        return render(request, 'blog/post_add.html')
