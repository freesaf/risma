#-*- coding: utf-8 -*-
import datetime
from django.db import models


class Offre(models.Model):   
    nomposte            = models.CharField("Poste ",blank=False,max_length=300)
    ref                 = models.CharField("Référence ",blank=False,max_length=100)
    date_de_cloture     = models.DateField() 
    intitule_du_poste   = models.CharField("Intitulé du poste ",blank=False,max_length=300)
    mission             = models.TextField("Mission ") 
    profil              = models.TextField("Profil ")
    division            = models.CharField(max_length=300,editable=False)
    secteur_dactivite   = models.CharField("Secteur d'activité ",blank=False,max_length=200)
    localisation        = models.CharField("Localisation ",blank=False,max_length=200)

    def __unicode__(self):              
        return self.nomposte

class CV(models.Model):
    nom               = models.CharField(max_length=250)
    prenom            = models.CharField(max_length=250)
    date_naissance    = models.DateField()
    ville             = models.CharField(max_length=50)
    telephone         = models.CharField(max_length=50)
    email             = models.EmailField()
    message           = models.TextField()
    cv                = models.FileField(upload_to="cv")
    lettre_motivation = models.FileField(upload_to="cv")
    date              = models.DateTimeField(auto_now_add=True)
    offre             = models.ForeignKey(Offre)
    formation         = models.CharField(max_length=250)

    def __unicode__(self):
        return self.nom

