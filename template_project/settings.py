import os  # isort:skip
gettext = lambda s: s
DATA_DIR = os.path.dirname(os.path.dirname(__file__))
"""
Django settings for template_project project.

Generated by 'django-admin startproject' using Django 2.1.13.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'tbv=ucrntmqsrr!c1y=4f7^4!)o54(@nm%m$it28s83pwl=@aj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'template-project-demo.herokuapp.com',
    'template-projectss.herokuapp.com',
    "*",
]
# https://template-projects.herokuapp.com/en/

# Application definition


print('test1')


ROOT_URLCONF = 'template_project.urls'


WSGI_APPLICATION = 'template_project.wsgi.application'

# Channels
# You must execute this command for it to work: docker run -p 6379:6379 -d redis:5
ASGI_APPLICATION = 'template_project.routing.application'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases




# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en'
USE_I18N = True
USE_L10N = True

TIME_ZONE = 'Europe/Sofia'

USE_I18N = True

USE_L10N = True

USE_TZ = True
LOGIN_URL = '/loginuser/'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
# STATIC_ROOT = '/tmp/staticfiles'
STATIC_ROOT = os.path.join(DATA_DIR, 'staticfiles')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'template_project', 'static'),
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

SITE_ID = 1


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                'sekizai.context_processors.sekizai',
                'django.template.context_processors.static',
                'cms.context_processors.cms_settings'
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader'
            ],
        },
    },
]


MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'axes.middleware.AxesMiddleware',
]

INSTALLED_APPS = [
    # 'admin_interface',
    'channels',
    'colorfield',
    'polymorphic',
    'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'cms',
    'nested_admin',
    'menus',
    'sekizai',
    'captcha',
    'treebeard',
    'djangocms_text_ckeditor',
    'filer',
    'bootstrap4',
    'easy_thumbnails',
    'djangocms_column',
    'djangocms_file',
    'djangocms_link',
    'djangocms_picture',
    'djangocms_style',
    'djangocms_snippet',
    'djangocms_googlemap',
    'djangocms_video',
    'template_project',
    'contrib.django_exes',
    'contrib.osm',
    'contrib.home',
    'contrib.import_export_file',
    'contrib.form_wizard',
    'contrib.crud_operation',
    'contrib.notifications',
    'contrib.sort_filter',
    'contrib.calculator',
    'contrib.abstract_model',
    'contrib.currencies',
    'contrib.admin_tricks',
    'contrib.validators',
    'contrib.accounts',
    'contrib.based_views',
    'contrib.petstagram',
    'contrib.django_polymorphic',
    'django_extensions',
    'axes',
    'import_export',
    'allauth.account',
    'osm_field',
    'rest_framework',
    'rest_framework.authtoken',
    'location_field.apps.DefaultConfig',
    'contrib.many_files.apps.ManyFilesConfig',
    'contrib.api_lead',
    'contrib.chat',
    'contrib.fibonacci_sequence',
]

DEFAULT_FROM_EMAIL = 'nikolay.veselinov@industria.tech'


LANGUAGES = [
    ('en', _('English')),
    ('bg', _('Bulgarian')),
]

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

CMS_LANGUAGES = {
    ## Customize this
    1: [
        {
            'code': 'en',
            'name': gettext('en'),
            'redirect_on_fallback': True,
            'public': True,
            'hide_untranslated': False,
        },
    ],
    'default': {
        'redirect_on_fallback': True,
        'public': True,
        'hide_untranslated': False,
    },
}

CMS_TEMPLATES = (
    ## Customize this
    ('fullwidth.html', 'Fullwidth'),
    ('sidebar_left.html', 'Sidebar Left'),
    ('sidebar_right.html', 'Sidebar Right'),
    ('placeholder.html', 'home'),
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {

}

# DATABASES = {
#     'default': {
#         'CONN_MAX_AGE': 0,
#         'ENGINE': 'django.db.backends.sqlite3',
#         'HOST': 'localhost',
#         'NAME': 'projectdb',
#         'USER': 'template_project',
#         'PASSWORD': 'template_project',
#         'PORT': '',
#         'USER': ''
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': os.environ.get('DB_NAME'),
#         'USER': os.environ.get('DB_USER'),
#         'PASSWORD': os.environ.get('DB_PASSWORD'),
#         'HOST': os.environ.get('DB_host'),
#         'PORT': os.environ.get('DB_PORT'),
#     }
# }

# Heroku DATABASES
# https://dashboard.heroku.com/apps/template-projects/settings
# postgres://idkcmkhjmjudfc:3729beae6bc45d182c82c145dd7c13bfae84e906453ef4c584bf178baf131a51@ec2-34-247-118-233.eu-west-1.compute.amazonaws.com:5432/d4uip67fidhegi
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'd4uip67fidhegi',
#         'HOST': 'ec2-34-247-118-233.eu-west-1.compute.amazonaws.com',
#         'PORT': '5432',
#         'USER': 'idkcmkhjmjudfc',
#         'PASSWORD': '3729beae6bc45d182c82c145dd7c13bfae84e906453ef4c584bf178baf131a51',
#     }
# }

# Heroku DATABASES 2
# https://dashboard.heroku.com/apps/template-projects/settings
# postgres://ohmlvutxklcdyw:f7cfe89edc588b435f3ac47dd3cec835b63eb18b6d287c4a28643335b0db4781@ec2-52-18-116-67.eu-west-1.compute.amazonaws.com:5432/d3i5t8d0c5q7n5
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd3i5t8d0c5q7n5',
        'HOST': 'ec2-52-18-116-67.eu-west-1.compute.amazonaws.com',
        'PORT': '5432',
        'USER': 'ohmlvutxklcdyw',
        'PASSWORD': 'f7cfe89edc588b435f3ac47dd3cec835b63eb18b6d287c4a28643335b0db4781',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'template_projectdb',
#         'USER': 'template_project',
#         'PASSWORD': 'template_project',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

MIGRATION_MODULES = {

}

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)

AUTHENTICATION_BACKENDS = [
    # AxesBackend should be the first backend in the AUTHENTICATION_BACKENDS list.
    'axes.backends.AxesBackend',

    # Django ModelBackend is the default authentication backend.
    'django.contrib.auth.backends.ModelBackend',
]

# Axes
AXES_LOGIN_FAILURE_LIMIT = 6
AXES_LOCK_OUT_BY_COMBINATION_USER_AND_IP = True
AXES_COOLOFF_TIME = 1
AXES_LOCKOUT_TEMPLATE = 'axes/lockout.html'
AXES_LOCKOUT_URL = '/lockout/'

# REST_FRAMEWORK = {
#     # Use Django's standard `django.contrib.auth` permissions,
#     # or allow read-only access for unauthenticated users.
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
#     ]
# }

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [],
    'DEFAULT_PERMISSION_CLASSES': [],
}

# LOGIN_REDIRECT_URL = '/'