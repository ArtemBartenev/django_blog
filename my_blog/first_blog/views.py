from django.shortcuts import render, redirect
from django.views import View

from .forms import TagForm
from .models import Post, Tag
from .utils import *


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'first_blog/index.html', context={'posts': posts})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'first_blog/tags_list.html', context={'tags': tags})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'first_blog/post_detail.html'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'first_blog/tag_detail.html'


class TagCreate(View):
    def get(self, request):
        form = TagForm()
        return render(request, 'first_blog/tag_create.html', context={'form': form})

    def post(self, request):
        bound_form = TagForm(request.POST)
        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        return render(request, 'first_blog/tag_create.html', context={'form': bound_form})