from settings.local import *


SEND_EMAILS = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'toddl',
        'TEST': {
            'NAME': 'toddl_test',
        },
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
