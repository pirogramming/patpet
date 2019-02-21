from django.db import models
from django.urls import reverse
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
from django.conf import settings


class Reccomendation:
    pass


class New:
    pass


class CommunicationPost(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False, null=False)

    title = models.CharField(max_length=20)
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    photo = ProcessedImageField(blank=True, upload_to='explore/post/%Y/%m/%d',
                                processors=[Thumbnail(300, 300)],
                                format='JPEG',
                                options={'quality': 60})

    class Meta:
        ordering = ['-created_at']

    def get_absolute_url(self):
        return reverse('explore:post_detail', args=[self.id])


class CommunicationComment(models.Model):
    post = models.ForeignKey(CommunicationPost, on_delete=models.CASCADE, related_name='comment_set')
    author = models.ForeignKey(CommunicationPost, on_delete=models.CASCADE)
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
