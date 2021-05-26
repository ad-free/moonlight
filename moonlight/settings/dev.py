# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import logging
from moonlight.settings.base import *
from django.utils.translation import gettext_lazy as _
from django.conf import settings

logger = logging.getLogger("")
logger.info("Starting on development environment")

DEBUG = True
ALLOWED_HOSTS += ["127.0.0.1", "localhost", "172.16.2.201"]

INSTALLED_APPS += []

TIME_ZONE = "Asia/Ho_Chi_Minh"
USE_TZ = True
USE_I18N = True

LANGUAGES = (
    ("en", _("English")),
    ("vn", _("Vietnamese")),
)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "verbose": {
            "format": "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            "datefmt": "%d/%b/%Y-%H:%M:%S",
        },
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "handlers": {
        "file": {
            "level": "INFO",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": os.path.join(settings.LOG_DIR, "api.log"),
            "when": "D",
            "interval": 1,
            "backupCount": 10,
            "formatter": "verbose",
        },
    },
    "loggers": {
        "": {"handlers": ["file"], "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"), },
        "root": {
            "handlers": ["file"],
            "level": os.getenv("DJANGO_LOG_LEVEL", "ERROR"),
        },
    },
}
