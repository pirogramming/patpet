from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext

from explore.models import CommunicationPost
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

    return render(request, 'explore/post_detail.html', {
        'post': post,
    })


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
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

