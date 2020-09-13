"""
Django settings for election project.

Generated by 'django-admin startproject' using Django 3.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import dj_database_url


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'n%!s8!ha0w^be$fn-mi#9m$^d6m89su2ux$_!fv^99phy=k*kt'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'n%!s8!ha0w^be$fn-mi#9m$^d6m89su2ux$_!fv^99phy=k*kt')
DEBUG = bool(os.environ.get('DJANGO_DEBUG', '') != 'False')
print('The key: ',SECRET_KEY)
print('The debug: ',DEBUG)
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'results',
    'accounts',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_registration',
    'corsheaders',
    'highcharts',
    'bootstrap4',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'election.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
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

WSGI_APPLICATION = 'election.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
       'default':{
            'ENGINE':'django.db.backends.postgresql_psycopg2',
            'NAME':'voting_db',
            'USER':'dbuser',
            'PASSWORD':'Bigibrahim1!',
            'HOST':'localhost',
            'PORT': '',

       }
       }

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT= os.path.join(BASE_DIR, 'static/')
STATICFILES_DIRS=[
    os.path.join(BASE_DIR, 'static/accounts'),
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'



# Medis files 
MEDIA_URL='media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


#Email settings
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'



#LOGIN_REDIRECT_URL='dashboard'
#LOGOUT_REDIRECT_URL= 'logout'

# Rest framework registration
REST_REGISTRATION = {
    'REGISTER_VERIFICATION_ENABLED': False,
    'RESET_PASSWORD_VERIFICATION_ENABLED': False,
    'REGISTER_EMAIL_VERIFICATION_ENABLED': False,
}


# Rest pagination
# REST_FRAMEWORK = {
#     'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
#     'PAGE_SIZE': 10
# }



# cors headers setting
CORS_ORIGIN_ALLOW_ALL = True



# Authentication backend
AUTHENTICATION_BACKENDS = (
'django.contrib.auth.backends.ModelBackend',
'accounts.authentication.EmailAuthBackend',
'accounts.authentication.PhoneNumberAuthBackend',
)

