from .drf_settings import *
from .common import *
from .base import DEBUG
if DEBUG:
    from .local import *
else:
    from .production import *






