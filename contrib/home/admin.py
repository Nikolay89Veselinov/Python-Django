from django.contrib import admin
from .models import UserProfile
from cms.extensions import TitleExtensionAdmin
from .models import RatingExtension
from cms.extensions import PageExtensionAdmin
from .models import IconExtension


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass


class IconExtensionAdmin(PageExtensionAdmin):
    pass

admin.site.register(IconExtension, IconExtensionAdmin)


class RatingExtensionAdmin(TitleExtensionAdmin):
    pass


admin.site.register(RatingExtension, RatingExtensionAdmin)