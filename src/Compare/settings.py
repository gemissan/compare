import os

from Compare import logging_settings


DEBUG = True
TEMPLATE_DEBUG = DEBUG

LOCAL_IPS = ("127.0.0.1",)

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

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

if DEBUG:
    AUTHENTICATION_BACKENDS = (
        'compareuser.backends.DummyAuthenticationBackend',
    ) + AUTHENTICATION_BACKENDS

LOGIN_URL = "login-user-view"

SESSION_ENGINE = 'django.contrib.sessions.backends.db'

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Warsaw'

# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'pl-PL'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = PROJECT_PATH + '/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_PATH, 'static')

STATIC_URL = '/static/'

STATICFILES_DIRS = ()

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = '*d7r0xg+_#-am2y3s)ef55=0j)l522v9^nf9_&i4u+&c_wyw=b'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'Compare.urls'

WSGI_APPLICATION = 'Compare.wsgi.application'

TEMPLATE_DIRS = (
    PROJECT_PATH + '/templates/',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
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
    'compareyoutube',
    'comparemain',
)

LOGGING_ROOT = logging_settings.LOGGING_ROOT
LOGGING = logging_settings.LOGGING
