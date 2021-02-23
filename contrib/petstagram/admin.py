from django.contrib import admin
from .models import Pet, Like, Comment


from django.contrib.admin.utils import unquote
from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.urls import path
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponse
from django.utils.safestring import mark_safe
from django.conf.urls import url


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):

    list_display = ('id', 'type', 'name', 'age', 'description', 'slug', 'image_url', 'get_admin_url')
    # prepopulated_fields = {"slug": ("name",)}
    
    def get_urls(self):
        info = self.model._meta.app_label, self.model._meta.model_name
        urls = super().get_urls()
        urlpatterns = [
            url(r'^(?P<object_id>\d+)/change/pdf/$',
                self.admin_site.admin_view(self.download_pdf),
                name='%s_%s_pdf' % info),
        ]
        return urlpatterns + urls

    def download_pdf(self, request, object_id):
        instance = self.get_object(request, unquote(object_id))
        return HttpResponse(instance.results_pdf(), content_type='application/pdf')


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('pet',)


admin.site.register(Comment)