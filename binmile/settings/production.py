# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'binmile',
        'USER': 'master',
        'PASSWORD': '726f01569f5d4b8dbfa7',
        'HOST': 'localhost',
        'PORT': '',
    }
}
