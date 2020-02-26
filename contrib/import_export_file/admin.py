from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportActionModelAdmin


from .models import Players


class PlayersResource(resources.ModelResource):

    class Meta:
        model = Players
        fields = ('name', 'region', 'score', 'rank', 'active', )

@admin.register(Players)
class PlayersAdmin(ImportExportActionModelAdmin):
    resource_class = PlayersResource
    list_display = ('name', 'region', 'score', 'rank', 'active', )


