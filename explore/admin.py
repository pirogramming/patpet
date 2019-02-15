from django.contrib import admin

from explore.models import CommunicationPost, CommunicationComment


@admin.register(CommunicationPost)
class CommunicationPostAdmin(admin.ModelAdmin):
    pass


@admin.register(CommunicationComment)
class CommunicationCommentAdmin(admin.ModelAdmin):
    pass