#-*- coding: utf-8 -*-
from django.db import models
from autoslug import AutoSlugField

from utils import *
from managers import PublicationManager


class Categorie(models.Model):
    nom = models.CharField(max_length=250)
    slug = AutoSlugField(populate_from='nom', unique=True)
    
    def __unicode__(self):
        return self.nom
    
    class Meta:
        #app_label = "Documents telecharges"
        #db_table = "file_uploader_Categorie"
        app_label = string_with_title("file_uploader", "Documents telecharges")
        
class Fichier(models.Model):
    titre = models.CharField(max_length=250) 
    fichier = models.FileField(upload_to='uploaded_files')
    image = models.ImageField(upload_to='uploaded_files')
    slug = AutoSlugField(populate_from='titre', unique=True)
    connexion_requise = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
    categorie = models.ForeignKey(Categorie, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    
    objects= models.Manager()
    publications = PublicationManager()
    
    def __unicode__(self):
        return self.titre
    
    @models.permalink
    def get_absolute_url(self):
        return ("fichier:download", [self.id])
    
    class Meta:
        app_label = string_with_title("file_uploader", "Documents telecharges")
    