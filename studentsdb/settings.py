"""
Django settings for studentsdb project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
from django.conf import global_settings

LANGUAGE_CODE = 'uk'    
TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
	"django.core.context_processors.request",
	"students.context_processors.groups_processor",
	"studentsdb.context_processors.students_proc",
)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_DIRS = (
	'/data/work/virtualenv/studentsdb/src/studentsdb/students/templates/students',
)	

PORTAL_URL = 'http://localhost:8000'

# email settings
# please, set here you smtp server details and your admin email
ADMIN_EMAIL='avkpol@yandex.ru'
EMAIL_HOST= 'smtp.gmail.com'
EMAIL_PORT= '465'
EMAIL_HOST_USER='andriykrav@gmail.com'
EMAIL_HOST_PASSWORD='Grysha1994'    
EMAIL_USE_TLS=False
EMAIL_USE_SSL=True


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$lrm#z+qs)(&2rkr)tnui0m0%7r%)s!)9ni$#ug_vjmce+5x%!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []



# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'students',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'studentsdb.urls'

WSGI_APPLICATION = 'studentsdb.wsgi.application'

#switch template pack on
CRISPY_TEMPLATE_PACK='bootstrap3'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

from db import DATABASES


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/



TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'media')




