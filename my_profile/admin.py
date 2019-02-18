from django.contrib import admin
from my_profile.models import Post, Tag, Comment, Archive

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Archive)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']