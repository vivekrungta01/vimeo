# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Vimeouser

class VimeouserAdmin(admin.ModelAdmin):
    list_display = ('name','url','paying_user','staff_pick_video','video_upload')

admin.site.register( Vimeouser, VimeouserAdmin)