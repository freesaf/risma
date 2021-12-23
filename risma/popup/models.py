#-*- coding: utf-8 -*-
from django.db import models


class Categorie(models.Model):
    nom = models.CharField(max_length=250)
    
    def __unicode__(self):
        return self.nom
    
class Popup(models.Model):
    titre       = models.CharField(max_length=150)
    image       = models.ImageField(upload_to='uploads/', null=True, blank=True)
    texte       = models.TextField(null=True, blank=True)
    lien        = models.CharField(max_length=250 , blank=True, null=True)
    date_debut  = models.DateTimeField()
    date_fin    = models.DateTimeField()
    categorie   = models.ForeignKey(Categorie)