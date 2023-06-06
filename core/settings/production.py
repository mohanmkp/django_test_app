
from . import base

SECRET_KEY = base.SECRET_KEY

ALLOWED_HOSTS = ["127.0.0.1"]

INSTALLED_APPS = base.INSTALLED_APPS + [
    "apps.seller",
    'apps.users',
    'apps.product',
    'apps.orders',

]

MIDDLEWARE = base.MIDDLEWARE + [


]


ROOT_URLCONF = 'core.urls'


DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "micro-ecom",
        "USER": "postgres",
        'PASSWORD': '12345',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    },

}

