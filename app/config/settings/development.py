from .base import *  # NOQA

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ["*"]
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

WAGTAIL_2FA_REQUIRED = False

ASSETS_DEBUG = True
ASSETS_AUTO_BUILD = True
