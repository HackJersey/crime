"""
Django settings for crime project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import dj_database_url
import django

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_S3_CUSTOM_DOMAIN = 'dycbt2qke8skt.cloudfront.net'

AWS_ACCESS_KEY_ID = os.environ.get('CRIME_AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.environ.get('CRIME_AWS_SECRET_KEY')

#Your Amazon Web Services storage bucket name, as a string.
AWS_STORAGE_BUCKET_NAME = "njsp-crime-reports"

AWS_S3_FILE_OVERWRITE = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATIC_HOST = os.environ.get('CRIME_DJANGO_STATIC_HOST', '')
#STATIC_URL = STATIC_HOST + '/static/'

ADMINS = (
    ('Tom Meagher', 'hello+crimeerrors@hackjersey.com'),
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'bootstrap_admin', # always before django.contrib.admin
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.staticfiles',
    'project.apps.crime',
    'phonenumber_field',
    'sendgrid',
#    'django_extensions',
    'timezone_field',
#    'selectable',
#    'tinymce',
#    'celery',
    'sortedm2m',
    'tastypie',
#    'countable_field',
#    'crispy_forms',
    'url_or_relative_url_field',
]

BOOTSTRAP_ADMIN_SIDEBAR_MENU = False

SITE_ID = 1

API_LIMIT_PER_PAGE = 50

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

MIDDLEWARE_CLASSES = (

)

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
                        'loaders': [('django.template.loaders.cached.Loader', [
                        'django.template.loaders.filesystem.Loader',
                        'django.template.loaders.app_directories.Loader',
                        ],
                    )],
        },
    },
]


WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Parse database configuration from $DATABASE_URL
DATABASES['default'] =  dj_database_url.config(default='postgres://tommeagher:@localhost/njcrime')

# Enable Connection Pooling (if desired)
DATABASES['default']['ENGINE'] = 'django_postgrespool'

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

#TODO set up admin redirect
#LOGIN_REDIRECT_URL = "/admin/executions/case"
LOGIN_URL = '/admin/login'


#email setup
EMAIL_BACKEND = 'sendgrid_backend.SendgridBackend'
SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')
SENDGRID_SANDBOX_MODE_IN_DEBUG = False
SERVER_EMAIL = 'hello+crimeerrors@hackjersey.com'
DEFAULT_FROM_EMAIL = 'Hack Jersey Crime <hello+crime@hackjersey.com>'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = os.environ.get('SENDGRID_USERNAME')
EMAIL_HOST_PASSWORD = os.environ.get('SENDGRID_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True

#TODO set up slack
'''
SLACK_URL = os.environ.get('KNELL_SLACK_URL')
SLACK_CHANNEL="#knell"
SLACK_SOCIAL_CHANNEL = "#social"
SLACK_USERNAME="knellbot"
SLACK_ICON_EMOJI=":bell:"
'''

#LOCKING = {'time_until_expiration': 120, 'time_until_warning': 60}

#TODO set up Celery task queue
'''
#Celery settings
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'

CELERY_RESULT_SERIALIZER = 'json'

BROKER_POOL_LIMIT = 1

CELERY_RESULT_BACKEND= 'djcelery.backends.database:DatabaseBackend'
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
'''

#todo setup TinyMCE
'''
#Rich Text Field settings through django-tinymce
TINYMCE_JS_URL = os.path.join(STATIC_URL, "tiny_mce/tinymce.min.js")
TINYMCE_DEFAULT_CONFIG = {
    'theme': 'advanced',
    'relative_urls': False,
    'content_css': ('/static/bootstrap/css/bootstrap.min.css'),
    'plugins':'code',
    'theme_advanced_buttons1': 'bold,italic,underline,bullist,numlist,blockquote,|,undo,redo,link,unlink,removeformat,|,formatselect,code',
    'theme_advanced_resizing': True,
    'theme_advanced_path': False,

}

TINYMCE_JS_ROOT = os.path.join(STATIC_ROOT, "tiny_mce/tinymce.min.js")

TINYMCE_SPELLCHECKER = False

TINYMCE_COMPRESSOR = True
'''

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
            }
        },
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
        },
        "mail_admins": {
        'level': 'WARNING',
        'class': 'django.utils.log.AdminEmailHandler'
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            'level': 'WARNING',
            'propagate': True,
        },

        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'WARNING',
            'propagate': True,
        }
    }
}

