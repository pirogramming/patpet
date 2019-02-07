from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User


def post_list(request):
    post = Post.objects.all()
    context = {
        'post': post,
    }
    return render(request, "home/layout.html", context)
