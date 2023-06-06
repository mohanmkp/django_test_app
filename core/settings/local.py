from . import base

SECRET_KEY = base.SECRET_KEY

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = base.INSTALLED_APPS + [
    "apps.seller",
    'apps.users',
    'apps.product',
    'apps.orders',
    # 'import_export',

]

MIDDLEWARE = base.MIDDLEWARE + [
    'middleware.agent_location.User_Track'

]


ROOT_URLCONF = 'core.urls'



DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': base.BASE_DIR / 'db.sqlite3',
        }
}







