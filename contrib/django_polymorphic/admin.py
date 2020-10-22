from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin, \
                              PolymorphicChildModelFilter, PolymorphicInlineSupportMixin
from nested_admin.nested import NestedModelAdmin, NestedTabularInline
from .models import Animals, Cat, Dog, Bird, Fish, Bear, ImageAnimals


class ImageAnimalsInline(PolymorphicInlineSupportMixin, NestedTabularInline):
    model = ImageAnimals
    extra = 1

class ModelAChildAdmin(PolymorphicChildModelAdmin):
    """ Base admin class for all child models """
    base_model = Animals  # Optional, explicitly set here.



@admin.register(Animals)
class AnimalsAdmin(PolymorphicParentModelAdmin):
    """ The parent model admin """
    base_model = Animals
    child_models = (Cat, Dog, Bird, Fish, Bear)
    list_filter = (PolymorphicChildModelFilter,)  # This is optional.
    list_display = ('animal', 'name', 'breed', 'age', 'abilities')

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

@admin.register(Dog)
class DogAdmin(ModelAChildAdmin, NestedModelAdmin):
    base_model = Dog
    inlines = (ImageAnimalsInline,)

@admin.register(Bird)
class BirdAdmin(ModelAChildAdmin, NestedModelAdmin):
    base_model = Bird
    inlines = (ImageAnimalsInline,)

@admin.register(Fish)
class FishAdmin(ModelAChildAdmin, NestedModelAdmin):
    base_model = Fish
    inlines = (ImageAnimalsInline,)

@admin.register(Bear)
class BearAdmin(ModelAChildAdmin, NestedModelAdmin):
    base_model = Bear
    inlines = (ImageAnimalsInline,)

