from django.db import models
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _
from utils import *
from django.template.defaultfilters import slugify
import os


here       = lambda x: os.path.join(os.path.abspath(os.path.dirname(__file__)), x) 
templates  = os.listdir( here("../templates/flatpages/") ) 


class Categorie(models.Model):
    nom = models.CharField(max_length=250)
    
    def __unicode__(self):
        return self.nom
    class Meta:
        app_label = string_with_title("custom_flatpages", "Menu")
    
    from django.template.defaultfilters import slugify
class FlatPage(models.Model):    
    title                 = models.CharField(_('titre'), max_length=200) 
    url                   = models.CharField(_('URL'), max_length=100, db_index=True)
    categorie             = models.ForeignKey(Categorie, null=True, blank=True)
    mot_cle               = models.CharField(max_length=300, blank=True, null=True)
    enable_comments       = models.BooleanField(_('enable comments'))
    template_name         = models.CharField(_('template name'),choices=[ ( str(templates[i]), str('flatpages/'+templates[i])) for i in range(len(templates)) ], max_length=70, blank=True,help_text=_("Example: 'flatpages/contact_page.html'. If this isn't provided, the system will use 'flatpages/default.html'."))
    registration_required = models.BooleanField(_('registration required'), help_text=_("If this is checked, only logged-in users will be able to view the page."))
    ordre                 = models.IntegerField(blank=True, null=True,default=0) 
    content               = models.TextField(_('contenu'), blank=True)
    image                 = models.ImageField(upload_to="images/flatpages", blank=True, null=True)
    image_thumbnail          = models.ImageField(upload_to="images/flatpages", blank=True, null=True)

    class Meta:
        app_label = string_with_title("custom_flatpages", "Menu")
        
        verbose_name = _('flat page')
        verbose_name_plural = _('flat pages')
        ordering = ('ordre','url')
        
    def save(self, *args, **kwargs):
        self.url = "/"+slugify(self.title)+"/"
        super(FlatPage, self).save(*args, **kwargs)
        
    def __unicode__(self):
        return u"%s -- %s" % (self.url, self.title)

    def get_absolute_url(self):
        return self.url

"""
class Contenu(models.Model):    
    content = models.TextField(_('contenu'), blank=True)
    image   = models.ImageField(upload_to="images/flatpages", blank=True, null=True)
    flatpage = models.ForeignKey(FlatPage)
    
    def __unicode__(self):
        return self.content
    class Meta:
        app_label = string_with_title("custom_flatpages", "Menu")
"""        