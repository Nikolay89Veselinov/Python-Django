from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model

from .models import UsersProfile

UserModel = get_user_model()

# @admin.register(UsersProfile)
class UsersProfileAdmin(admin.StackedInline):
    model = UsersProfile
    verbose_name_plural = 'Profile'
    extra = 1


# @admin.site.unregister(UserModel)
# @admin.register(UserModel)
class UserAdmin(BaseUserAdmin):
    inlines = (
        UsersProfileAdmin,
    )



admin.site.unregister(UserModel)
admin.site.register(UserModel, UserAdmin)