from django.urls import path, re_path
from my_profile import views

app_name = 'my_profile'

urlpatterns = [
    path('post/new/', views.post_new, name='post_new'),
    re_path(r'^(?P<username>\w+)/post/list/$', views.my_post_list, name='my_post_list'),
    re_path(r'^(?P<pk>\d+)/post/edit/$', views.post_edit, name='post_edit'),
    re_path(r'^(?P<pk>\d+)/post/delete/$', views.post_delete, name='post_delete'),
    re_path(r'^(?P<pk>\d+)/comment/new/$', views.comment_new, name='comment_new'),
    re_path(r'^(?P<pk>\d+)/comment/delete/$', views.comment_delete, name='comment_delete'),
]