from django.urls import path, re_path
from my_profile import views

urlpatterns = [
    path('', views.post_new_button),
    path('post_new/', views.post_new, name='post_new'),
    path('post_list/', views.post_list),
]