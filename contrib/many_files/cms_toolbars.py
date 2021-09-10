from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool
from .models import File


class FileToolbar(CMSToolbar):

    def populate(self):
        self.toolbar.get_or_create_menu(
            'file_cms_integration-files',  # a unique key for this menu
            'FileToolBar',                        # the text that should appear in the menu
            )
# register the toolbar
toolbar_pool.register(FileToolbar)