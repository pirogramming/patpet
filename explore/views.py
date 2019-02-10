from django.shortcuts import render
from my_profile.models import Post


def post_list(request):
    post = Post.objects.all()
    context = {
        'post': post,
    }
    return render(request, "explore/layout.html", context)
