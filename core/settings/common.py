import os
from . import base


TEMPLATES = base.TEMPLATES


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

WSGI_APPLICATION = base.WSGI_APPLICATION


AUTH_USER_MODEL = 'users.User'


AUTH_PASSWORD_VALIDATORS = base.AUTH_PASSWORD_VALIDATORS

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = False


STATIC_URL = 'static/'

STATICFILES_DIRS = [
    base.BASE_DIR / "static"
]

STATIC_ROOT = base.BASE_DIR / 'static_files'

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(base.BASE_DIR, 'media/')

