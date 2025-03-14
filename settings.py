"""
Django settings for pfmrestapi project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR=os.path.join(BASE_DIR, 'template')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_DIR = [os.path.join(BASE_DIR, 'media')]


# Check if the file exists and is not a directory
if os.path.exists('C:\\djangoex\\pfmrestapi\\media\\images') and not os.path.isdir('C:\\djangoex\\pfmrestapi\\media\\images'):
    # Delete the file
    os.remove('C:\\djangoex\\pfmrestapi\\media\\images')
# Create the directory
if not os.path.exists('C:\\djangoex\\pfmrestapi\\media\\images'):
    os.makedirs('C:\\djangoex\\pfmrestapi\\media\\images')
    
    
# Check if the file exists and is not a directory
if os.path.exists('C:\\djangoex\\pfmrestapi\\media\\videos') and not os.path.isdir('C:\\djangoex\\pfmrestapi\\media\\videos'):
    # Delete the file
    os.remove('C:\\djangoex\\pfmrestapi\\media\\videos')
# Create the directory
if not os.path.exists('C:\\djangoex\\pfmrestapi\\media\\videos'):
    os.makedirs('C:\\djangoex\\pfmrestapi\\media\\videos')
    
    
# Check if the file exists and is not a directory
if os.path.exists('C:\\djangoex\\pfmrestapi\\media\\documents') and not os.path.isdir('C:\\djangoex\\pfmrestapi\\media\\documents'):
    # Delete the file
    os.remove('C:\\djangoex\\pfmrestapi\\media\\documents')
# Create the directory
if not os.path.exists('C:\\djangoex\\pfmrestapi\\media\\documents'):
    os.makedirs('C:\\djangoex\\pfmrestapi\\media\\documents')
    
    
# Check if the file exists and is not a directory
if os.path.exists('C:\\djangoex\\pfmrestapi\\media\\audios') and not os.path.isdir('C:\\djangoex\\pfmrestapi\\media\\audios'):
    # Delete the file
    os.remove('C:\\djangoex\\pfmrestapi\\media\\audios')
# Create the directory
if not os.path.exists('C:\\djangoex\\pfmrestapi\\media\\audios'):
    os.makedirs('C:\\djangoex\\pfmrestapi\\media\\audios')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-0wox_b-2nqy2%rvyumz14r24#g$(kk&7#w&=wtrff9+g+=t(1t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
    'rest_framework'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pfmrestapi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR,],
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

WSGI_APPLICATION = 'pfmrestapi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS=[
    BASE_DIR/'static',
]

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
