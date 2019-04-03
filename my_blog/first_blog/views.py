from django.shortcuts import render
from .models import Post


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'first_blog/index.html', context={'posts': posts})

def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'first_blog/post_detail.html', context={'post': post})