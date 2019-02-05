from django.urls import path, re_path
from home import views

urlpatterns = [
    path('', views.home),
]
