from django.db import models

class Post(models.Model):
    content = models.TextField(verbose_name='내용')
    photo = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)  # 길이 제한 있는 문자열
    updated_at = models.DateTimeField(auto_now=True)  # 길이 제한 없는 문자열