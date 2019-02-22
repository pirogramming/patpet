import re
from datetime import datetime, timezone
from django.conf import settings
from django.db import models
from django.shortcuts import get_object_or_404
from django.urls import reverse
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

from accounts.models import Archive


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False, null=False)
    content = models.TextField(blank=True)
    photo = models.ImageField(blank=False)
    tag_set = models.ManyToManyField('Tag', blank='True')
    created_at = models.DateTimeField(auto_now_add=True)  # 길이 제한 있는 문자열
    updated_at = models.DateTimeField(auto_now=True)  # 길이 제한 없는 문자열
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked', blank=True)
    archive = models.ManyToManyField(Archive, related_name='saved', blank=True, null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Post (PK: {self.pk}, Author: {self.author.username})'

    def get_absolute_url(self):
        return reverse('home:post_list')

    def tag_save(self):
        tags = re.findall(r'#(\w+)\b', self.content)

        if not tags:
            return

        for t in tags:
            tag, tag_created = Tag.objects.get_or_create(name=t)
            self.tag_set.add(tag)  # NOTE: ManyToManyField 에 인스턴스 추가

    def time_interval(self):
        now = datetime.now(timezone.utc)
        time_interval = now - self.created_at
        return time_interval

    def total_likes(self):
        return self.likes.count()


class Tag(models.Model):
    name = models.CharField(max_length=140, unique=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False)
    content = models.CharField(max_length=40, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Comment (PK: {self.pk}, Author: {self.author.username})'
