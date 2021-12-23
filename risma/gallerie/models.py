#-*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _
from autoslug import AutoSlugField

class Gallerie(models.Model):
    titre = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='titre')
    
    def __unicode__(self):
        return self.titre
        
class Photo(models.Model):
    photo = models.ImageField(upload_to="photos")
    titre = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    gallerie = models.ForeignKey(Gallerie)
    url = models.URLField(null=True, blank=True, verify_exists=False)
    
