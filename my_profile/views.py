from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from my_profile.models import Post, Comment
from .forms import PostForm, CommentForm

@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            post.tag_save()
            messages.success(request, 'posts successfully uploaded')
            return redirect('my_profile:my_post_list', request.user)
    else:
        form = PostForm()
    return render(request, 'my_profile/post_form.html', {
        'form': form,
        })


@login_required
def my_post_list(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    post_list = user.post_set.all()
    comment_form = CommentForm()

    return render(request, 'my_profile/my_post_list.html', {
        'post_list': post_list,
        'username': username,
        'comment_form': comment_form,
    })


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            messages.success(request, 'posts successfully edited')
            redirect('my_profile:my_post_list', request.user)
    else:
        form = PostForm(instance=post)
    return render(request, 'my_profile/post_form.html', {
        'form': form,
        })


@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user or request.method == 'GET':
        messages.warning(request, '잘못된 접근입니다.')
        return redirect('/home/post_list/')

    if request.method == 'POST':
        post.delete()
        messages.success(request, 'posts successfully deleted')
        return redirect('my_profile:my_post_list', request.user)


@login_required
def comment_new(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=pk)
        content = request.POST.get('content')
        if not content:
            return HttpResponse('댓글 내용을 입력하세요', status=400)

        Comment.objects.create(
            post=post,
            author=request.user,
            content=content
        )
        messages.success(request, 'comments successfully uploaded')
        next = request.POST.get('next-e','/')
        return HttpResponseRedirect(next)



@login_required
def comment_delete(request, pk):
    if request.method == 'POST':
        next = request.POST.get('next-d', '/')
        comment = get_object_or_404(Comment, pk=pk)
        comment.delete()
        messages.success(request, 'comments successfully deleted')
        return HttpResponseRedirect(next)