"""
Django settings for travelsite project.

Generated by 'django-admin startproject' using Django 2.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import django_heroku
import dj_database_url
from decouple import config


# For the environment variable
from dotenv import load_dotenv
load_dotenv()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG')

ALLOWED_HOSTS = ['https://travel-agent-visa.herokuapp.com/', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'travel',
    'travelblog',
    'jobs',
    'marketing',
    'accounts',
    'tinymce',
    'ckeditor',
    'crispy_forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    # AWS app
    'storages',
    # authentication apps
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django_countries',
]

# for the crispy-form
# CRISPY_TEMPLATE_PACK = 'boostrap4'
CRISPY_TEMPLATE_PACK = 'bootstrap4'


MIDDLEWARE = [
     'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'travelsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # os.path.join(BASE_DIR,'travelblog/templates/travelblog'),
            os.path.join(BASE_DIR,'travelsite/templates/travelsite'),
            os.path.join(BASE_DIR,'travel/templates/travel'),
            os.path.join(BASE_DIR,'travelsite/templates/travelsite/account'),

        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'travelsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
database_USER= os.environ.get('USER')
database_PASSWORD = os.environ.get('PASSWORD')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd5j8gbnfmt7lv8',
        'USER': '{}'.format(database_USER),
        'PASSWORD': '{}'.format(database_PASSWORD),
        'HOST': 'ec2-3-212-90-231.compute-1.amazonaws.com'
    }
}


db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles'),

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'travelsite/static'),
    os.path.join(BASE_DIR, 'travel/static'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
django_heroku.settings(locals())

# for aw3 configuration

# to redirect user to the dashboard after login
LOGIN_REDIRECT_URL= 'travel:dashboard'

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME  = os.environ.get('AWS_STORAGE_BUCKET_NAME ')

# for django storages settings

AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None

DEFAULT_FILE_STORAGE= 'storages.backends.s3boto3.S3Boto3Storage'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_S3_HOST = 'us-east-2.amazonaws.com'
AWS_S3_REGION_NAME = 'us-east-2'

AWS_S3_SIGNATURE_VERSION = 's3v4'


# this is for tinyMCE Configuration
TINYMCE_DEFAULT_CONFIG = {
    # 'height': 360,
    # 'width': 1120,
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    'theme': 'modern',
    'plugins': '''
            textcolor save link image media preview codesample contextmenu
            table code lists fullscreen  insertdatetime  nonbreaking
            contextmenu directionality searchreplace wordcount visualblocks
            visualchars code fullscreen autolink lists  charmap print  hr
            anchor pagebreak
            ''',
    'toolbar1': '''
            fullscreen preview bold italic underline | fontselect,
            fontsizeselect  | forecolor backcolor | alignleft alignright |
            aligncenter alignjustify | indent outdent | bullist numlist table |
            | link image media | codesample |
            ''',
    'toolbar2': '''
            visualblocks visualchars |
            charmap hr pagebreak nonbreaking anchor |  code |
            ''',
    'contextmenu': 'formats | link image',
    'menubar': True,
    'statusbar': True,
    }

# this is for the dajango authentification
AUTHENTICATION_BACKENDS = [   
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',    
]
SITE_ID = 1

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
