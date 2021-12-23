#-*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from risma.gallerie.models import *

from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^ckeditor\.fields\.RichTextField"])

class Hotel(models.Model):
    nom         = models.CharField(max_length=250, null=True, blank=True)
    slug        = AutoSlugField(populate_from='nom', unique=True)
    logo        = models.ImageField(upload_to='uploads/', null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    galerie     = models.ForeignKey(Gallerie, null= True)

    def __unicode__(self):
        return self.nom