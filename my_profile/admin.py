from django.contrib import admin
from my_profile.models import Post, Tag, Comment

admin.site.register(Post)
admin.site.register(Comment)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']