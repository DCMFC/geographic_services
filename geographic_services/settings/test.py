from .base import *  # noqa
from .base import mongoengine

mongoengine.disconnect()

DEBUG = True

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
