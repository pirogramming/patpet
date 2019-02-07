import re
from django.conf import settings
from django.db import models
from django.urls import reverse


class Post(models.Model):
    content = models.TextField()
    photo = models.ImageField()
    tag_set = models.ManyToManyField('Tag', blank='True')
    created_at = models.DateTimeField(auto_now_add=True)  # 길이 제한 있는 문자열
    updated_at = models.DateTimeField(auto_now=True)  # 길이 제한 없는 문자열

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('home:post_detail', args=[self.id])

    def tag_save(self):
        tags = re.findall(r'#(\w+)\b', self.content)

        if not tags:
            return

        for t in tags:
            tag, tag_created = Tag.objects.get_or_create(name=t)
            self.tag_set.add(tag)  # NOTE: ManyToManyField 에 인스턴스 추가

class Tag(models.Model):
    name = models.CharField(max_length=140, unique=True)

    def __str__(self):
        return self.name