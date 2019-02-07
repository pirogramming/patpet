from django.contrib import admin
from my_profile.models import Post, Tag

admin.site.register(Post)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']