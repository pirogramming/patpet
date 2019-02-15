from django.urls import path, re_path
from home import views

app_name = 'home'

urlpatterns = [
    path('post_list/', views.post_list, name='post_list'),
    ]