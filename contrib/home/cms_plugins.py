from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from .models import CategoryPlugin

@plugin_pool.register_plugin
class CMSCategoryPlugin(CMSPluginBase):
    model = CategoryPlugin
    module = ('Category')
    name = 'Category'
    render_template = 'plugins/category_plugin.html'
    allow_children = True
    child_classes = ["CMSChildren_plugin"]
    def render(self, context, instance, placeholder):
        context.update({
            'title': instance.title,
            'description': instance.description,
            'image': instance.image,
            'created': instance.created,
            'active': instance.active,
            'instance': instance,
        })
        return context

@plugin_pool.register_plugin
class CMSChildren_plugin(CMSPluginBase):
    render_template = 'plugins/children_plugin.html'
    name = "Children Plugin"
    module = "Children Plugin"
    require_parent = True
    parent_classes = ["CMSCategoryPlugin"]
    allow_children = False
    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context
