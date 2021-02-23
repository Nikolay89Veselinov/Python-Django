from django.contrib import admin
from django.contrib.admin.utils import unquote
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, \
                              PolymorphicChildModelFilter, PolymorphicInlineSupportMixin
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
from nested_admin.nested import NestedModelAdmin, NestedTabularInline
from django.http import HttpResponse
from django.conf.urls import url
from .models import Animals, Cat, Dog, Bird, Fish, Bear, ImageAnimals


class ImageAnimalsInline(PolymorphicInlineSupportMixin, NestedTabularInline):
    model = ImageAnimals
    extra = 1

class ModelAChildAdmin(PolymorphicChildModelAdmin):
    """ Base admin class for all child models """
    base_model = Animals  # Optional, explicitly set here.



@admin.register(Animals)
class AnimalsAdmin(PolymorphicParentModelAdmin):

    def download_pdf(self, obj=None):
        return mark_safe(f'<a href="{self.get_admin_url()}pdf/">Download PDF</a>')
    download_pdf.short_description = 'Download PDF'

    """ The parent model admin """
    base_model = Animals
    child_models = (Cat, Dog, Bird, Fish, Bear)
    list_filter = (PolymorphicChildModelFilter,)  # This is optional.
    list_display = ('id', 'animal', 'name', 'breed', 'age', 'abilities', download_pdf)

    def animal(self, obj):
        return obj.get_real_instance().__str__()
    animal.short_description = 'Animal'

    def name(self, obj):
        return obj.get_real_instance().name
    name.short_description = 'Name'

    def age(self, obj):
        return obj.get_real_instance().age
    age.short_description = 'Age'

    def abilities(self, obj):
        return obj.get_real_instance().abilities
    abilities.short_description = 'abilities'

@admin.register(Cat)
class CatAdmin( ModelAChildAdmin, NestedModelAdmin):
    base_model = Cat
    inlines = (ImageAnimalsInline,)
    # show_in_index = True  # makes child model admin visible in main admin site

    def get_urls(self):
        
        info = self.model._meta.app_label, self.model._meta.model_name
        urlpatterns = [
            url(r'^(?P<object_id>\d+)/change/pdf/$',
                self.admin_site.admin_view(self.download_pdf),
                name='%s_%s_pdf' % info),
        ]
        urlpatterns.extend(super().get_urls())
        
        return urlpatterns
    def download_pdf(self, request, object_id):
        instance = self.get_object(request, unquote(object_id))
        return HttpResponse(instance.results_pdf(), content_type='application/pdf')

@admin.register(Dog)
class DogAdmin(ModelAChildAdmin, NestedModelAdmin):
    base_model = Dog
    inlines = (ImageAnimalsInline,)

    def get_urls(self):
        
        info = self.model._meta.app_label, self.model._meta.model_name
        urlpatterns = [
            url(r'^(?P<object_id>\d+)/change/pdf/$',
                self.admin_site.admin_view(self.download_pdf),
                name='%s_%s_pdf' % info),
        ]
        urlpatterns.extend(super().get_urls())
        
        return urlpatterns

    def download_pdf(self, request, object_id):
        instance = self.get_object(request, unquote(object_id))
        return HttpResponse(instance.results_pdf(), content_type='application/pdf')

@admin.register(Bird)
class BirdAdmin(ModelAChildAdmin, NestedModelAdmin):
    base_model = Bird
    inlines = (ImageAnimalsInline,)

    def get_urls(self):
        
        info = self.model._meta.app_label, self.model._meta.model_name
        urlpatterns = [
            url(r'^(?P<object_id>\d+)/change/pdf/$',
                self.admin_site.admin_view(self.download_pdf),
                name='%s_%s_pdf' % info),
        ]
        urlpatterns.extend(super().get_urls())
        
        return urlpatterns

    def download_pdf(self, request, object_id):
        instance = self.get_object(request, unquote(object_id))
        return HttpResponse(instance.results_pdf(), content_type='application/pdf')


@admin.register(Fish)
class FishAdmin(ModelAChildAdmin, NestedModelAdmin):
    base_model = Fish
    inlines = (ImageAnimalsInline,)

    def get_urls(self):
        
        info = self.model._meta.app_label, self.model._meta.model_name
        urlpatterns = [
            url(r'^(?P<object_id>\d+)/change/pdf/$',
                self.admin_site.admin_view(self.download_pdf),
                name='%s_%s_pdf' % info),
        ]
        urlpatterns.extend(super().get_urls())
        return urlpatterns

    def download_pdf(self, request, object_id):
        instance = self.get_object(request, unquote(object_id))
        return HttpResponse(instance.results_pdf(), content_type='application/pdf')


@admin.register(Bear)
class BearAdmin(ModelAChildAdmin, NestedModelAdmin):
    base_model = Bear
    inlines = (ImageAnimalsInline,)

    def get_urls(self):
        
        info = self.model._meta.app_label, self.model._meta.model_name
        urlpatterns = [
            url(r'^(?P<object_id>\d+)/change/pdf/$',
                self.admin_site.admin_view(self.download_pdf),
                name='%s_%s_pdf' % info),
        ]
        urlpatterns.extend(super().get_urls())
        return urlpatterns

    def download_pdf(self, request, object_id):
        instance = self.get_object(request, unquote(object_id))
        return HttpResponse(instance.results_pdf(), content_type='application/pdf')
        