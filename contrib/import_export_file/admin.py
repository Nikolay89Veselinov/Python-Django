from django.contrib import admin

from import_export import resources, fields
from import_export.admin import ImportExportActionModelAdmin


from .models import Players


class PlayersResource(resources.ModelResource):
    region = fields.Field(column_name='region')
    game = fields.Field(column_name='game')
    last_name = fields.Field(column_name='last_name')

    class Meta:
        model = Players
        fields = ('id', 'game', 'name', 'score', 'rank' ,'region', 'active')
        export_order = fields

    def dehydrate_rank(self, players):
        if players.rank:
            return 'Master'
        return ''

@admin.register(Players)
class PlayersAdmin(ImportExportActionModelAdmin):
    resource_class = PlayersResource
    list_display = ('name', 'region', 'score', 'rank', 'active', )


