from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from my_profile.models import Post
from my_profile.forms import CommentForm

@login_required
def post_list(request):
    post = Post.objects.all()
    comment_form = CommentForm()
    like_all = request.user.liked.all()
    # print(like_all)

    context = {
        'post': post,
        'comment_form': comment_form,
        'like_all': like_all,
    }
    return render(request, "home/layout.html", context)
