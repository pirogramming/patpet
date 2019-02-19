from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from accounts.models import Archive
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
            return redirect(post)
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
            return redirect('/home/post_list/') #namespace:name
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
        messages.success(request, '삭제완료')
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
        # print(request.path)
        return redirect('home:post_list')

        # return HttpResponseRedirect(request.POST['path'])
        # return HttpResponseRedirect(request.POST.get('path'))

@login_required
def comment_delete(request, pk):
    if request.method == 'POST':
        comment = get_object_or_404(Comment, pk=pk)
        comment.delete()
        messages.success(request, '삭제완료')
        return redirect('home:post_list')

@login_required
def like_post(request, pk):
    post_to_like = get_object_or_404(Post, pk=pk)
    act_user = request.user
    # print(post_to_like.likes.filter(pk=pk))
    is_liked = post_to_like.likes.filter(id=act_user.id).exists()
    # print(is_liked)
    if post_to_like.likes.filter(id=act_user.id).exists():
        # print('여기다여기')
        # print(post_to_like.likes.filter(pk=pk))
        post_to_like.likes.remove(act_user)
    else:
        post_to_like.likes.add(act_user)
        messages.success(request, "Like this post")
    # # print(data)
    # t = user_profile.followed_by.all()
    # # print(t)

    return redirect('home:post_list')
        # 'is_liked':is_liked,

@login_required
def arc_add(request, post_id, arc_id):
    post_to_add = get_object_or_404(Post, pk=post_id)
    arc = get_object_or_404(Archive, pk=arc_id)
    # print(arc)
    # print(post_to_add)
    # print(post_to_add.archive.all())
    if post_to_add.archive.filter(id=arc_id).exists():
        post_to_add.archive.remove(arc)
        print('삭제')
    else:
        post_to_add.archive.add(arc)
        print('추가')

    return redirect('home:post_list')

