from django.shortcuts import render
from my_profile.models import Post


def explore_post_list(request):
    return render(request, "explore/layout.html")
