# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Vimeouser(models.Model):
    name = models.CharField( max_length = 100)
    url=models.URLField(max_length = 250)
    paying_user=models.BooleanField()
    staff_pick_video=models.BooleanField()
    video_upload=models.BooleanField()
    def __unicode__(self):
        return self.name
    
    
    
    
    
