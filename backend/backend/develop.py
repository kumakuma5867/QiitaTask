from .base import *

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'default': {
            '()': 'django.utils.log.ServerFormatter',
            'format': '%(levelname)s: [%(server_time)s] %(message)s a',
        },
        'file_format': {
            "format": ", ".join([
                "[%(levelname)s]",
                "%(asctime)s",
                "%(pathname)s",
                "%(lineno)d",
                "%(message)s",
            ])
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'log/develop.log'),
            'formatter': 'file_format',
            'when': 'D',
            'interval': 1,
            'backupCount': 7
        }
    },
    'loggers': {
        'backend': {
            'handlers': ['file'], 'level': 'DEBUG'
        }
    }
}
