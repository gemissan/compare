import os


LOGGING_ROOT = '/var/log/django/compare'

if not os.path.isdir(LOGGING_ROOT):
    os.makedirs(LOGGING_ROOT)

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
            'format': '%(asctime)s %(levelname)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'path': {
            'format': '%(levelname)s %(pathname)s:%(lineno)s\n\t%(message)s'
        },
        'simple': {
            'format': '%(asctime)s %(levelname)s %(name)s %(message)s'
        },
        'minimal': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'NOTSET',
            'class': 'logging.StreamHandler',
            'formatter': 'minimal'
        },
        'root_rotating_file': {
            'level': 'NOTSET',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGGING_ROOT, 'main.log'),
            'mode': 'a',
            'maxBytes': 1024 * 1024,
            'backupCount': 10,
            'formatter': 'verbose'
        },
        'error_rotating_file': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGGING_ROOT, 'error.log'),
            'maxBytes': 1024 * 1024,
            'backupCount': 0,
            'formatter': 'verbose'
        },
        'request_rotating_file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGGING_ROOT, 'request.log'),
            'maxBytes': 5 * 1024 * 1024,
            'backupCount': 5,
            'formatter': 'simple'
        },
        'signals_rotating_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGGING_ROOT, 'signals.log'),
            'maxBytes': 1024 * 1024,
            'backupCount': 1,
            'formatter': 'simple'
        },
        'middleware_rotating_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGGING_ROOT, 'middleware.log'),
            'maxBytes': 1024 * 1024,
            'backupCount': 1,
            'formatter': 'simple'
        },
        'authentication_rotating_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGGING_ROOT, 'authentication.log'),
            'maxBytes': 1024 * 1024,
            'backupCount': 1,
            'formatter': 'simple'
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
            'propagate': False,
        },
        'signals': {
            'handlers': ['signals_rotating_file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'middleware': {
            'handlers': ['middleware_rotating_file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'authentication': {
            'handlers': ['authentication_rotating_file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'ws': {
            'handlers': ['root_rotating_file'],
            'level': 'DEBUG',
        }
    }
}

log_modules = ('compareutils', 'compareuser', 'comparelist', 'comparemain')

for log_module in log_modules:
    handler = log_module + '_rotating_file_handler'
    filename = os.path.join(LOGGING_ROOT, log_module + '.log')
    LOGGING['handlers'][handler] = {
        'level': 'NOTSET',
        'class': 'logging.handlers.RotatingFileHandler',
        'filename': filename,
        'maxBytes': 1024 * 1024,
        'backupCount': 1,
        'formatter': 'path',
        'filters': ['require_debug_true']
    }
    LOGGING['loggers'][log_module] = {
        'handlers': [handler],
        'level': 'DEBUG',
        'propagate': True
    }