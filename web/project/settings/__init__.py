from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ['DEBUG']

# STATICFILES_DIRS.append(
#     os.path.join(PROJECT_DIR, 'static', os.environ['THEME_VERSION']),
# )

for template_engine in TEMPLATES:
    template_engine['OPTIONS']['debug'] = os.environ['TEMPLATE_DEBUG']

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASS'],
        'HOST': os.environ['DB_SERVICE'],
        'PORT': os.environ['DB_PORT'],
    }
}


try:
    from .local import *
except ImportError:
    pass
