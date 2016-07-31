"""
Django settings for djapp project.

Generated by 'django-admin startproject' using Django 1.9.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '026@=coy_w)%@on9rm3sv!6^31&xcmw#r5ce0fklky^p8+zfok'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Application definition

INSTALLED_APPS = [
]

MIDDLEWARE_CLASSES = [
]

ROOT_URLCONF = 'djapp.urls'

WSGI_APPLICATION = 'djapp.wsgi.application'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'loggers': {
        'django.request': {
            'propagate': 0,
            'handlers': ['stream'],
            'level': 'CRITICAL',
        },
    },
    'handlers': {
        'stream': {
            'class': 'logging.StreamHandler',
        },
    },
}
