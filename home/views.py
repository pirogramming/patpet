from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from accounts.models import Archive
from my_profile.models import Post
from my_profile.forms import CommentForm

@login_required
def post_list(request):
    post = Post.objects.all()
    comment_form = CommentForm()
    like_all = request.user.liked.all()
    # print(like_all)
    arc = Archive.objects.filter(owner=request.user)
    print(1)
    print(arc)
    print(2)
    context = {
        'post': post,
        'comment_form': comment_form,
        'like_all': like_all,
        'all_arc': arc,
    }
    return render(request, "home/layout.html", context)
