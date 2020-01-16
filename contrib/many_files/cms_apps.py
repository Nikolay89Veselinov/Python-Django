from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from .urls import urlpatterns


@apphook_pool.register
class FileApp(CMSApp):
    name = 'File App'
    app_name = 'file-app'

    def get_urls(self, page=None, language=None, **kwargs):
        return urlpatterns
