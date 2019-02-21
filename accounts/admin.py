from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import Profile, Message


#
# class CustomUserInline(admin.StackedInline):
#     model = CustomUser
#     can_delete = False
#     verbose_name_plural = 'CustomUser'
#
# # Define a new User admin
# class UserAdmin(BaseUserAdmin):
#     inlines = (CustomUserInline,)
#
# # Re-register UserAdmin
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

# @admin.register(Follow)
# class FollowAdmin(admin.ModelAdmin):
#     pass

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass