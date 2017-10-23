# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from . models import Show, Pod
admin.site.register(Show)
admin.site.register(Pod)
