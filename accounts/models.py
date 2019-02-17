from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User, PermissionsMixin, AbstractUser
from django.db import models
from django.conf import settings



class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    introduce = models.TextField(max_length=200)
    follows = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followed_by', symmetrical=False, blank=True)
    pic = models.ImageField(blank=True)
    recommend = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='recommended', symmetrical=False, blank=True)



User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])


# class Recomendation(models.Model):
#     recomend = models.ManyToManyField(settings.AUTH_USER_MODEL, symmetrical=False, blank=True)
#
#
#
# class Follow(models.Model):
#     user = models.ForeignKey('auth.User', related_name='friends', on_delete=models.CASCADE)
#     target = models.ForeignKey('auth.User', related_name='followers', on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         unique_together = ('user', 'target')