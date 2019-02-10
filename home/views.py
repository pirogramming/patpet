from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from my_profile.models import Post
from django.conf import settings

@login_required
def post_list(request):
    post = Post.objects.all()
    context = {
        'post': post,
    }
    return render(request, "home/layout.html", context)
