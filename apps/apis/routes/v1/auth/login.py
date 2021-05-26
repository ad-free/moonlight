# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.shortcuts import render
from django.views import View


class Login(View):
    template = 'auth/login.html'

    def get(self, request):
        return render(request, self.template, context={})
