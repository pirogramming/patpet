from django.urls import path, re_path
from explore import views


app_name= 'explore'
urlpatterns = [
    path('', views.post_list, name='explore'),
    # path('explore/', views.post_list, name='explore'),
    ]
