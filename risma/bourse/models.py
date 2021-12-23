#-*- coding: utf-8 -*-
from django.db import models
from django.conf import settings

"""class Cours(models.Model):
    date    = models.DateField()
    dernier = models.FloatField()
    premier = models.FloatField()
    plus_haut   = models.FloatField()
    plus_bas    = models.FloatField()
    volume  = models.FloatField()
    capitaux    = models.FloatField()
    date_import = models.DateTimeField(auto_now_add=True, null=True)

    def __unicode__(self):
        return  u"%s" % (self.date)"""

class Cour(models.Model):
    date    = models.DateField()
    dernier = models.FloatField()
    premier = models.FloatField()
    plus_haut   = models.FloatField()
    plus_bas    = models.FloatField()
    volume  = models.FloatField()
    capitaux    = models.FloatField()
    date_import = models.DateTimeField(auto_now_add=True, null=True)

    def __unicode__(self):
        return  u"%s" % (self.date)


"""class Indicateur(models.Model):
    name        = models.CharField(max_length=250, null=True, blank=True)
    last_quote  = models.CharField(max_length=250, null=True, blank=True)
    currency    = models.CharField(max_length=250, null=True, blank=True)
    variation   = models.CharField(max_length=250, null=True, blank=True)
    curseur     = models.CharField(max_length=250, null=True, blank=True)
    date        = models.CharField(max_length=250, null=True, blank=True)
    isin        = models.CharField(max_length=250, null=True, blank=True)
    market_center   = models.CharField(max_length=250, null=True, blank=True)
    #date_import = models.DateTimeField(auto_now_add=True, null=True)

    def __unicode__(self):
        return  u"%s" % (self.last_quote)"""

class Indicator(models.Model):
    last_quote  = models.CharField(max_length=250, null=False, blank=False)
    currency    = models.CharField(max_length=250, null=False, blank=False)
    variation   = models.CharField(max_length=250, null=False, blank=False)
    curseur     = models.CharField(max_length=250, null=False, blank=False)
    date        = models.CharField(max_length=250, null=False, blank=False)
    isin        = models.CharField(max_length=250, null=False, blank=False)
    market_center   = models.CharField(max_length=250, null=False, blank=False)

    def __unicode__(self):
        return  u"%s" % (self.last_quote)
