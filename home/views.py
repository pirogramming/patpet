from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

from accounts.forms import ArchiveForm
from accounts.models import Archive
from my_profile.models import Post
from my_profile.forms import CommentForm

@login_required
def post_list(request):
    post = Post.objects.all()
    comment_form = CommentForm()
    like_all = request.user.liked.all()
    arc = Archive.objects.filter(owner=request.user)
    arcform = ArchiveForm()
    following = request.user.followed_by.all()
    t = [request.user.id, ]
    for i in following:
        t.append(i.id)
    # print(t)
    # print('요기요')
    # print(following)
    # print(post)
    follow_post = Post.objects.filter(author__in = t)
    # print(follow_post)

    context = {
        'post': follow_post,
        'comment_form': comment_form,
        'like_all': like_all,
        'all_arc': arc,
        'form': arcform,
    }
    return render(request, "home/layout.html", context)

def make_archive(request):
    if request.method == 'POST':
        arc = request.POST.get('archive')
        if not arc:
            return HttpResponse('null', status=400)
        Archive.objects.create(
            owner=request.user,
            archive=arc,
        )
        return redirect('home:post_list')
