from .base import * # NOQA

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# 终端打印SQL语句
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
    'console': {
        'level': 'DEBUG',
        'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG',
        },
    }
}