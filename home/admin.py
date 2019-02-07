from django.contrib import admin
from home.models import Post, Tag

admin.site.register(Post)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']