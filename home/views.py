from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User

def home(request):
    post = Post.objects.all()
    author = User()
    context = {
        'post': post,
    }
    return render(request, "home/layout.html", context)
