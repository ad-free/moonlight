# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=200)
    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.CharField(max_length=200, null=True, default=_("Anonymous"))


    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Cameras')

    
    def save(self, *args, **kwargs):
        super(Project, self).save(*args, *kwargs)

    def __str__(self) -> str:
        return self.name

    def __unicode__(self) -> str:
        return u'{}'.format(self.name)
