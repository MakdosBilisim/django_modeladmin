import os

tarih                                               = "02.01.2019"

BASE_DIR                                            = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


DEBUG                                               = False                                          ### runserver da True olmalı




STATIC_URL                                          = '/static/'

# STATIC_ROOT                                         = os.path.join(BASE_DIR, 'static')          ### Sunucu için
# ALLOWED_HOSTS                                       = ["modeladmin.alanadi.com"]                ### Sunucu için
ALLOWED_HOSTS                                       = ["*"]                                       ### Local için
STATIC_ROOT                                         = ''                                          ### Lokal için
STATICFILES_DIRS                                    = (os.path.join(BASE_DIR, 'static'),)         ### Lokal için
SECURE_SSL_REDIRECT                                 = False                                       ### https e yönlendirme

INSTALLED_APPS                                      = [
                                                        'django.contrib.admin',
                                                        'django.contrib.auth',
                                                        'django.contrib.contenttypes',
                                                        'django.contrib.sessions',
                                                        'django.contrib.messages',
                                                        'django.contrib.staticfiles',
                                                        'kayitlar.apps.KayitlarConfig',
                                                    ]

# DATABASES                                           = {
#                                                                'default': {
#                                                                    'ENGINE': 'django.db.backends.postgresql_psycopg2',
#                                                                    'NAME': 'dbadi',
#                                                                    'USER': 'modeladminuser',
#                                                                    'PASSWORD': 'modeladminpass',
#                                                                    'HOST': '192.168.101.202',
#                                                                    'PORT': '5432',
#                                                                     'CONN_MAX_AGE': 600,
#                                                                }
#                                                        }


DATABASES                                           = {
                                                            'default': {
                                                                'ENGINE': 'django.db.backends.sqlite3',
                                                                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
                                                            }
                                                        }


MIDDLEWARE                                          = [
                                                            'django.middleware.security.SecurityMiddleware',
                                                            'django.contrib.sessions.middleware.SessionMiddleware',
                                                            'django.middleware.common.CommonMiddleware',
                                                            'django.middleware.csrf.CsrfViewMiddleware',
                                                            'django.contrib.auth.middleware.AuthenticationMiddleware',
                                                            'django.contrib.messages.middleware.MessageMiddleware',
                                                            'django.middleware.clickjacking.XFrameOptionsMiddleware',
                                                        ]

TEMPLATES                                           = [
                                                        {
                                                            'BACKEND': 'django.template.backends.django.DjangoTemplates',
                                                            'DIRS': [os.path.join(BASE_DIR, 'templates')],
                                                            'APP_DIRS': True, ## özel html ler için True olmalı.
                                                            'OPTIONS': {
                                                                'context_processors': [
                                                                    'django.template.context_processors.debug',
                                                                    'django.template.context_processors.request',
                                                                    'django.contrib.auth.context_processors.auth',
                                                                    'django.contrib.messages.context_processors.messages',
                                                                    'django.template.context_processors.media',
                                                                ],
                                                            },
                                                        },
                                                    ]

ROOT_URLCONF                                        = 'modeladmin.urls'
LANGUAGE_CODE                                       = 'tr_TR'
TIME_ZONE                                           = 'Europe/Istanbul'
USE_I18N                                            = True
USE_L10N                                            = True
USE_TZ                                              = False
DATA_UPLOAD_MAX_NUMBER_FIELDS                       = 99999 # Toplu silme işleminde limit

WSGI_APPLICATION                                    = 'modeladmin.wsgi.application'
#######################################################################################################
if DEBUG:
                                                        INTERNAL_IPS = ('78.187.60.13', '127.0.0.1')
                                                        MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
                                                        INSTALLED_APPS += ('debug_toolbar',)
                                                        DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False}
                                                        DEBUG_TOOLBAR_PANELS = [
                                                            'debug_toolbar.panels.sql.SQLPanel',
                                                            'debug_toolbar.panels.staticfiles.StaticFilesPanel',
                                                            'debug_toolbar.panels.templates.TemplatesPanel',
                                                        ]

SECRET_KEY                                          = 's-&qy=k7&yze*_$jz2lbb%2=k9+kv+3w0n%xe-&h_+a356vbn455%-)%adwe'
#######################################################################################################
# import codecs
# import logging
# import sys
#
# logging.basicConfig(level=logging.INFO, format='%(message)s', handlers=[logging.FileHandler(os.path.join(BASE_DIR, "djangoLog.log"), 'w', 'utf-8')])
# sys.stdout                                          = codecs.getwriter("utf-8")(sys.stdout.detach())
# LOGGING                                             = {
#                                                             'version': 1,
#                                                             'disable_existing_loggers': False,
#                                                             'handlers': {
#                                                                 'log_to_stdout': {
#                                                                     'level': 'DEBUG',
#                                                                     'class': 'logging.StreamHandler',
#                                                                     'stream': sys.stdout,
#                                                                 },
#                                                             },
#                                                             'loggers': {
#                                                                 'main': {
#                                                                     'handlers': ['log_to_stdout'],
#                                                                     'level': 'DEBUG',
#                                                                     'propagate': True,
#                                                                 }
#                                                             }
#                                                         }
########################################