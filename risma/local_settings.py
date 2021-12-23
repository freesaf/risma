DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'c200_risma',                      # Or path to database file if using sqlite3.
        'USER': 'c200_risma',                      # Not used with sqlite3.
        'PASSWORD': '3Cmyz%43',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

EMAIL = "contact@xxxxxxxxxxx.ma"
EMAIL_HOST = 'smtp.xxxxxx.ma'
EMAIL_HOST_USER = 'contact@xxxx.ma'
EMAIL_HOST_PASSWORD = 'xxxxxxxxxxxx'
EMAIL_USE_TLS = False
EMAIL_PORT = 25

MEDIA_URL = "/site_media/"
ADMIN_MEDIA_PREFIX = '/site_media/media/'
DEBUG = True
