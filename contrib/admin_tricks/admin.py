from django.contrib import admin

from .models import AdminTricks
from django.core import serializers
from django.http import HttpResponse



@admin.register(AdminTricks)
class AdminTricksAdmin(admin.ModelAdmin):
    list_display = ('upper_case_name', 'colored_name', 'eng', 'empty_phone', 'email', 'month', 'decade_born_in', 'active')
    date_hierarchy = 'birthday'
    list_filter = ('first_name' ,'eng', 'email')
    list_display_links = ('eng',)
    empty_value_display = '-empty-'
    search_fields = ('email',)
    list_editable = ('month',)
    radio_fields = {"month": admin.HORIZONTAL}
    # admin.site.empty_value_display = '(None)'
    fieldsets = (
        (None, {
            'fields': (('first_name', 'last_name','eng'), 'month', 'birthday', 'phone', 'email', 'active'),
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('color_code',),
        }),
    )

    actions = ['rename_first_name', 'export_as_json']
    # actions = None
    def rename_first_name(self, request, queryset):
        self.message_user(request, "Changed status on {} orders".format(queryset.count()))
        for obj in queryset:
            queryset.update(first_name='Rename ' + obj.first_name)
    rename_first_name.short_description = "Rename first name"

    def upper_case_name(self, obj):
        return (f"{obj.first_name} {obj.last_name}").upper()
    upper_case_name.short_description = 'Full name'

    def empty_phone(self, obj):
         return obj.phone

    def get_changeform_initial_data(self, request):
        return {'first_name': 'Gosho',
                'last_name': 'Petrov',
                'phone': '0897455768',
            }

    def export_as_json(self, request, queryset):
        response = HttpResponse(content_type="application/json")
        serializers.serialize("json", queryset, stream=response)
        return response

    def has_add_permission(self, request):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    empty_phone.empty_value_display = 'unknown'

