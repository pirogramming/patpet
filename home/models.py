from django.conf import settings
from django.db import models


class Post(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    photo = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)  # 길이 제한 있는 문자열
    updated_at = models.DateTimeField(auto_now=True)  # 길이 제한 없는 문자열