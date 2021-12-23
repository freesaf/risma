#-*- coding: utf-8 -*-
import os
import sys
import re
sys.path.append(os.getcwd())
here = lambda x: os.path.join(os.path.abspath(os.path.dirname(__file__)), x)

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'c200_risma',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
TIME_ZONE = 'Africa/Casablanca'

# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'fr'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
LANGUAGES = (('fr', u'Français'), ('en', u'English'),)

SITE_URL = "http://risma.com"


MEDIA_ROOT =  here('site_media')
STATIC_URL = MEDIA_URL = '/site_media/'
ADMIN_MEDIA_PREFIX = '/media/'

SECRET_KEY = 'xm+qi8elz-8#2j81$@b+)z4ew4(mfzxw_b(lkn#3$9(1cjuei9'

TEMPLATE_LOADERS = (
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.filesystem.Loader',
)

MIDDLEWARE_CLASSES = (
    #'localeurl.middleware.LocaleURLMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'pagination.middleware.PaginationMiddleware',
    #'django.middleware.locale.LocaleMiddleware',
    #'django.core.context_processors.i18n',
)


ROOT_URLCONF = 'risma.urls'


TEMPLATE_DIRS = (
    here("templates")
)

INSTALLED_APPS = (
    #'localeurl',
    'django.contrib.auth',
    'django.contrib.comments',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'ckeditor',
    'constance',
    'constance.backends.database',
    'custom_flatpages',
    'disqus', #utilisé dans : media
    'django_extensions',
    'django_mobile',
    'django_xmlrpc',
    'easy_thumbnails',
    'file_uploader',
    'mediatheque',
    #'modeltranslation',
    'mptt', #utilisé dans : media
    'pagination',
    'ckeditor',
    'south',
    'sentry',
    'indexer',
    'paging',
    'contact',
    'recrutement',
    'gallerie',
    'news',
    'newsletter',
    'tagging', #utilisé dans : media
    #'taggit',
    'presse',
    'hotels',
    'zinnia',
    'social_sharing',
    'popup',
    #'scrapy'
    'bourse',
)

TEMPLATE_CONTEXT_PROCESSORS =(
    "django.core.context_processors.request", 
    "django.core.context_processors.auth", 
    "django.core.context_processors.media", 
    "django.core.context_processors.debug", 
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.i18n",
    "constance.context_processors.config",
)

EMAIL = ""
EMAIL_HOST = ''
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
EMAIL_USE_TLS = True

CKEDITOR_MEDIA_PREFIX = "/site_media/ckeditor/"
CKEDITOR_UPLOAD_PATH = here("site_media/uploads")
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [
                [      'Undo', 'Redo',
                  '-', 'Bold', 'Italic', 'Underline',
                  '-', 'Link', 'Unlink', 'RemoveFormat'
                ],
                [      
                  '-', 'BulletedList', 'NumberedList',
                  '-', 'Cut','Copy','Paste','PasteText','PasteFromWord', 'TextColor'
                ]
            ],
    },
}

MODELTRANSLATION_TRANSLATION_REGISTRY = "translation"
LOCALEURL_USE_ACCEPT_LANGUAGE = True


try:
    from local_settings import *
except ImportError, exp:
    pass

#django-constance
CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'
CONSTANCE_CONFIG = {
    'TELEPHONE': ('05 22 33 44 55', u'Numéro de téléphone'),
    'EMAIL' : ('votreadresse@domaine.com', u'C\'est sur cette adresse e-mail que vous receverez les emails de vos clients'),
    'METHODE_PAIEMENT' : ('Paiement à la livraison', u'Méthode de paiement')
}
CONSTANCE_DATABASE_CACHE_BACKEND = 'memcached://127.0.0.1:11211/'

#CKEditor
CKEDITOR_MEDIA_PREFIX = "/site_media/ckeditor/"
CKEDITOR_UPLOAD_PATH = here("site_media/uploads")
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [
                [      'Undo', 'Redo', 'Format',
                  '-', 'Bold', 'Italic', 'Underline',
                  '-', 'Image', 'Link', 'Unlink', 'RemoveFormat', 'Source'
                ],
                [      
                  '-', 'BulletedList', 'NumberedList', 'CreateDiv',
                  '-', 'Cut','Copy','Paste','PasteText','PasteFromWord', 'TextColor'
                ]
            ],
    },
    'blog': {
        'toolbar': [
                [      'Undo', 'Redo', 'Format', 'FontSize',
                  '-', 'JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock',
                  '-', 'Bold', 'Italic', 'Underline',
                  '-', 'Link', 'Unlink', 'RemoveFormat',
                ],
                [      
                  '-', 'BulletedList', 'NumberedList',
                  '-', 'Cut','Copy','Paste','PasteText','PasteFromWord', 'TextColor',
                  '-', 'Image', 'Flash', 'Source'
                ]
            ],
    },
    'flatpages': {
        'toolbar': [
                [      'Undo', 'Redo', 'Format',
                  '-', 'Bold', 'Italic', 'Underline',
                  '-', 'Image', 'Link', 'Unlink', 'RemoveFormat'
                ],
                [      
                  '-', 'BulletedList', 'NumberedList', 'CreateDiv',
                  '-', 'Cut','Copy','Paste','PasteText','PasteFromWord', 'TextColor', 'Source'
                ]
            ],
    },
}

#django-disqus, utilisé dans : media
DISQUS_API_KEY = 'iJDVeBf0kSB7iUtlhC902QUmShtY2ku6yYaLd2fFmk8dN0uiImbvpjKceejmmAXo'
DISQUS_WEBSITE_SHORTNAME = ''


