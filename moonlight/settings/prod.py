# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import base
from django.conf import settings


base.DEBUG = False
base.ALLOWED_HOSTS = []

base.INSTALLED_APPS += [
    'apps.apis',
]

base.TIME_ZONE = 'Asia/Ho_Chi_Minh'
base.USE_TZ = True
base.USE_I18N = True
