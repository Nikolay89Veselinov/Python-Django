# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls import include, url
from django.urls import path
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve
from django.utils.decorators import method_decorator

from allauth.account.views import LoginView

from axes.decorators import axes_dispatch
from axes.decorators import axes_form_invalid

from rest_framework import routers, serializers, viewsets

from contrib.home.views import home, url_with_arguments, reverse_views
from contrib.many_files.views import files
from contrib.osm.views import map
from contrib.django_exes.views import Login
from contrib.django_exes.forms import AxesLoginForm
from contrib.api_lead.views import UserViewSet, ItemViewSet
from contrib.form_wizard.views import ContactWizard, formset_view, form_messages, widget_form
from contrib.notifications.views import get_notification
from contrib.sort_filter.views import filter, get_country, get_pub
from contrib.calculator.views import get_response
from contrib.currencies.views import exchange_rate, convert_currencies
from contrib.validators.views import validator



LoginView.dispatch = method_decorator(axes_dispatch)(LoginView.dispatch)
LoginView.form_invalid = method_decorator(axes_form_invalid)(LoginView.form_invalid)

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'items', ItemViewSet)


urlpatterns = [
    path('api/', include(router.urls), name='apii'),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': {'cmspages': CMSSitemap}}),
    path('en/<str:username>/<slug:article_value>/<str:id>', home, name='home_user_article'),
    path('en/reverse/', reverse_views, name='reverse_views'),
    path('en/', home, name='home'),
    path('en/url_with_arguments/', include('contrib.home.urls'), name='url_with_arguments'),
    path('en/files/', files, name='files'),
    path('en/map/', map, name='map'),
    path('en/wizard/', ContactWizard.as_view(), name='wizard'),
    path('en/formset/', formset_view, name='formset'),
    path('login/', Login.as_view(), name='login'),
    url(r'^accounts/login/$', LoginView.as_view(form_class=AxesLoginForm), name='account_login'),
    url(r'^accounts/', include('allauth.urls')),
    path('en/form_messages/', form_messages, name='form_message'),
    path('en/widget_form/', widget_form, name='widget_form'),
    path(r'captcha/', include('captcha.urls')),
    path('en/notifications/', get_notification, name='notifications'),
    path('en/filter/', filter, name='filter'),
    path('en/get_city/', get_country, name='get_country'),
    path('en/get_pub/', get_pub, name='get0pub'),
    path('en/response/', get_response, name='get_response'),
    path('en/exchange_rate/', exchange_rate, name='Exchange_rate'),
    path('ajax/convert_currencies', convert_currencies, name="convert_currencies"),
    path('en/validators/', validator, name='validators'),
    path('en/crud/', include('contrib.crud_operation.urls'), name='crud'),
    # url(r'^locked/$', locked_out, name='locked_out'),
]

urlpatterns += i18n_patterns(
    url(r'^admin/', admin.site.urls),  # NOQA
    url(r'^', include('cms.urls')),

)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = [
        url(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ] + staticfiles_urlpatterns() + urlpatterns
