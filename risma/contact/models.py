#-*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _

class Contact(models.Model):
    nom          = models.CharField(max_length=250)
    prenom       = models.CharField(max_length=250)
    organisation = models.CharField(max_length=250, null=True)
    sujet        = models.CharField(max_length=250, blank=True)
    email        = models.EmailField()
    telephone    = models.CharField(null=True, max_length=250)
    message      = models.TextField()
    date_envoi   = models.DateField(auto_now_add=True, editable=False)

    def __unicode__(self):
        return "- %s" % self.sujet