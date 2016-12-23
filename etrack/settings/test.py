from .common import *

DEBUG = False
TEMPLATE_DEBUG = False

SECRET_KEY = "TESTING_DO_NOT_USE_IN_PRODUCTION"

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'etrack_test',
    }
}

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)
