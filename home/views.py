from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from my_profile.models import Post
from my_profile.forms import CommentForm

@login_required
def post_list(request):
    post = Post.objects.all()
    comment_form = CommentForm()
    context = {
        'post': post,
        'comment_form': comment_form,
    }
    return render(request, "home/layout.html", context)
