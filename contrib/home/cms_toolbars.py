from cms.toolbar_pool import toolbar_pool
from cms.extensions.toolbar import ExtensionToolbar
from django.utils.translation import gettext_lazy as _
from .models import IconExtension
from .models import RatingExtension
from cms.utils import get_language_list


@toolbar_pool.register
class IconExtensionToolbar(ExtensionToolbar):
    # defines the model for the current toolbar
    model = IconExtension

    def populate(self):
        # setup the extension toolbar with permissions and sanity checks
        current_page_menu = self._setup_extension_toolbar()

        # if it's all ok
        if current_page_menu:
            # retrieves the instance of the current extension (if any) and the toolbar item URL
            page_extension, url = self.get_page_extension_admin()
            if url:
                # adds a toolbar item in position 0 (at the top of the menu)
                current_page_menu.add_modal_item(_('Page Icon'), url=url,
                    disabled=not self.toolbar.edit_mode_active, position=0)


@toolbar_pool.register
class RatingExtensionToolbar(ExtensionToolbar):
    # defines the model for the current toolbar
    model = RatingExtension

    def populate(self):
        # setup the extension toolbar with permissions and sanity checks
        current_page_menu = self._setup_extension_toolbar()

        # if it's all ok
        if current_page_menu and self.toolbar.edit_mode_active:
            # create a sub menu labelled "Ratings" at position 1 in the menu
            sub_menu = self._get_sub_menu(
                current_page_menu, 'submenu_label', 'Ratings', position=1
                )

            # retrieves the instances of the current title extension (if any)
            # and the toolbar item URL
            urls = self.get_title_extension_admin()

            # we now also need to get the titleset (i.e. different language titles)
            # for this page
            page = self._get_page()
            titleset = page.title_set.filter(language__in=get_language_list(page.node.site_id))

            # create a 3-tuple of (title_extension, url, title)
            nodes = [(title_extension, url, title.title) for (
                (title_extension, url), title) in zip(urls, titleset)
                ]

            # cycle through the list of nodes
            for title_extension, url, title in nodes:

                # adds toolbar items
                sub_menu.add_modal_item(
                    'Rate %s' % title, url=url, disabled=not self.toolbar.edit_mode_active
                    )