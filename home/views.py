from django.shortcuts import render
from .models import Post

def home(request):
    post = Post.objects.first()
    context = {
        'post': post,
    }
    return render(request, "home/layout.html", context)
