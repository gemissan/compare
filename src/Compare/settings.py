import os
from os import path

DEBUG = True
TEMPLATE_DEBUG = DEBUG

LOCAL_IP = ("127.0.0.1",)

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

ADMINS = (
          ('Grzesiek', 'grzegorz.swica@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'compare',
        'USER': 'compare',
        'PASSWORD': 'compare',
        'HOST': 'localhost',
        'PORT': '',
    }
}

AUTH_USER_MODEL = 'compareuser.CompareUser'

AUTHENTICATION_BACKENDS = ('compareuser.backends.DummyAuthenticationBackend',
                           'django.contrib.auth.backends.ModelBackend')

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Warsaw'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'pl-PL'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = PROJECT_PATH + '/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = PROJECT_PATH + '/static/'

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '*d7r0xg+_#-am2y3s)ef55=0j)l522v9^nf9_&i4u+&c_wyw=b'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'compareutils.middleware.DisableDebugSiteMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'Compare.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'Compare.wsgi.application'

TEMPLATE_DIRS = (
    PROJECT_PATH + '/templates/'
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.messages.context_processors.messages',
    'django.contrib.auth.context_processors.auth',
    )

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    
    'south',
    
    'compareuser',
    'compareobject',
    'comparelist',
    'compareutils',
)

LOGGING_ROOT = '/var/log/django/compare'

if not path.isdir(LOGGING_ROOT):
    os.makedirs(LOGGING_ROOT)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue'
        }
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'path': {
            'format': '%(levelname)s %(pathname)s:%(lineno)s\n\t%(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'NOTSET',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'root_rotating_file': {
            'level': 'NOTSET',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': path.join(LOGGING_ROOT, 'main.log'),
            'mode': 'a',
            'maxBytes': 1024 * 1024,
            'backupCount': 10,
            'formatter': 'verbose'
        },
        'error_rotating_file': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': path.join(LOGGING_ROOT, 'error.log'),
            'maxBytes': 1024 * 1024,
            'backupCount': 0,
            'formatter': 'verbose'
        },
        'request_rotating_file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': path.join(LOGGING_ROOT, 'request.log'),
            'maxBytes': 5 * 1024 * 1024,
            'backupCount': 5,
            'formatter': 'simple'
        },
        'utils_rotating_file': {
            'level': 'NOTSET',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': path.join(LOGGING_ROOT, 'utils.log'),
            'maxBytes': 1024 * 1024,
            'backupCount': 1,
            'formatter': 'path',
            'filters': ['require_debug_true'],
        },
        'users_rotating_file': {
            'level': 'NOTSET',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': path.join(LOGGING_ROOT, 'users.log'),
            'maxBytes': 1024 * 1024,
            'backupCount': 1,
            'formatter': 'path',
            'filters': ['require_debug_true'],
        },
        'mail_admins': {
            'level': 'CRITICAL',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        '': {
            'handlers': ['console', 'root_rotating_file', 'error_rotating_file', 'mail_admins'],
            'level': 'WARNING',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['request_rotating_file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'compareutils': {
            'handlers': ['utils_rotating_file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'compareuser': {
            'handlers': ['users_rotating_file'],
            'level': 'DEBUG',
            'propagate': True,
        }
    }
}
