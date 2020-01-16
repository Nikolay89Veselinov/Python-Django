from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from .models import CategoryPlugin

@plugin_pool.register_plugin
class CMSCategoryPlugin(CMSPluginBase):
    model = CategoryPlugin
    module = ('Category')
    name = 'Category'
    render_template = 'plugins/category_plugin.html'

    def render(self, context, instance, placeholder):
        context.update({
            'title': instance.title,
            'description': instance.description,
            'image': instance.image,
            'created': instance.created,
            'active': instance.active,
        })
        return context
