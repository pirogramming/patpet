from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext

from explore.models import CommunicationPost, CommunicationComment
from .forms import PostForm

from my_profile.models import Post
from .forms import CommentForm
from django.contrib import messages


def post_list(request):
    post = CommunicationPost.objects.all()

    return render(request, "explore/post_list.html", {
        'post_list': post,
    })


def post_detail(request, id):
    post = get_object_or_404(CommunicationPost, id=id)
    form = CommentForm

    return render(request, 'explore/post_detail.html', {
        'post': post,
        'form': form,
    })


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save()
            return redirect('/explore/')
    else:
        form = PostForm()
    return render(request, 'explore/post_form.html', {
        'form': form,
    })


def post_edit(request, id):
    post = get_object_or_404(CommunicationPost, id=id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            post = form.save()

            return redirect('explore:post_detail', id=id)
    else:
        form = PostForm(instance=post)
    return render(request, 'explore/post_form.html', {
        'form': form,
    })


def post_delete(request, id):
    post = get_object_or_404(CommunicationPost, id=id)

    if request.method == 'POST':
        post.delete()
        return redirect('/explore/', request.user)


@login_required
def my_communication_list(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    post_list = user.communicationpost_set.all()

    return render(request, 'explore/my_communication_list.html', {
        'post_list': post_list,
        'username': username,
    })


@login_required
def comment_new(request, id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=id)
        content = request.POST.get('content')
        if not content:
            return HttpResponse('댓글 내용을 입력하세요', status=400)

        CommunicationComment.objects.create(
            post=post,
            author=request.user,
            content=content
        )
        form = CommentForm()
        return redirect(request, 'post:post_detail', {
            'form':form
        })


@login_required
def comment_delete(request, id):
    if request.method == 'POST':
        next = request.POST.get('next-d', '/')
        comment = get_object_or_404(CommunicationComment, id=id)
        comment.delete()
        return HttpResponseRedirect(next)
