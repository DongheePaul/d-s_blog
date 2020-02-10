from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Post

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
