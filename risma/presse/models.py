#-*- coding: utf-8 -*-
from django.db import models
from autoslug import AutoSlugField


class Diffusion(models.Model):
    nom = models.CharField(max_length=250)
    
    def __unicode__(self):
        return self.nom
    
class CommuniquePresse(models.Model):
    titre        = models.CharField(max_length=250)
    description  = models.TextField()
    fichier      = models.FileField(upload_to="presse", null=True, blank=True)
    fichier_en   = models.FileField(upload_to="presse", null=True, blank=True)
    fichier_ar   = models.FileField(upload_to="presse", null=True, blank=True)
    date         = models.DateField(null=True, blank=True)
    media        = models.CharField(max_length=250,blank=True)
    media_photo  = models.ImageField(upload_to="presse", null=True,blank=True)
    lien         = models.URLField(null=True, blank=True)
    slug         = AutoSlugField(populate_from='titre', unique=True)
    revue_presse = models.BooleanField(blank=True)
    diffusion    = models.ForeignKey(Diffusion, null=True, blank=True)
    titre_fichier1        = models.CharField(max_length=250, null=True, blank=True)
    titre_fichier2       = models.CharField(max_length=250, null=True, blank=True)
    fichier2      = models.FileField(upload_to="presse", null=True, blank=True)
    
    def __unicode__(self):
        return self.titre
    
    class Meta:
        ordering = ["-date"]
        
    @models.permalink
    def get_absolute_url(self):
        return ('communique_details', [self.slug])
    

    
"""   
class Presse(models.Model):
    titre = models.CharField(max_length=250)
    date = models.DateField(null=True, blank=True)
    extrait = models.TextField()
    media = models.CharField(max_length=250)
    media_photo = models.ImageField(upload_to="presse", null=True)
    diffusion = models.ForeignKey(Diffusion, null=True, blank=True)
    lien = models.URLField(null=True, blank=True)
    fichier = models.FileField(upload_to="presse", null=True, blank=True)
    slug = AutoSlugField(populate_from='titre', unique=True)
    
    def __unicode__(self):
        return self.titre
    
    @models.permalink
    def get_absolute_url(self):
        return ('presse_details', [self.slug])
    
    class Meta:
        ordering = ["-date"]
"""        
        
