from django.shortcuts import render, redirect
from my_profile.forms import PostForm
from home.models import Post

def post_new_button(request):
    return render(request, 'my_profile/layout.html')

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            post.tag_save()
            return redirect(post)
    else:
        form = PostForm()
    return render(request, 'my_profile/post_form.html', {
        'form': form,
        })