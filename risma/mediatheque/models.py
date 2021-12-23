#-*- coding: utf-8 -*-
from autoslug import AutoSlugField
import cStringIO
from PIL import Image
import simplejson
import urllib, urllib2
from urlparse import urlparse

from django.core.files import File
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from managers import EmbededManager, ImageManager,VideoManager


video_help_text = u"Fournir URL d'une vidéo provenant de Dailymotion/Vimeo ou Youtube, ou un son Soundcloud"

class ContenuMediaAbstract(models.Model):
    """ Contenu media qui va avec le post (image, vidéo ou audio)."""
    titre = models.CharField(max_length=250, null=True, blank=True)
    image = models.ImageField(upload_to='uploads/', null=True, blank=True)
    video = models.URLField(_(u'Vidéo/Son'), null=True, blank=True, 
                        help_text=video_help_text)
    old_url = models.CharField(max_length=250, editable=False, null=True)
    thumbnail_url = models.ImageField(upload_to='uploads/', null=True, blank=True, editable=False)    
    integration = models.TextField(null=True, blank=True)
    
    objects = models.Manager()
    images =  ImageManager()
    embed = EmbededManager()
    videos = VideoManager()
    
    class Meta:
        abstract = True
        
    def __unicode__(self):
        return self.type_media
    
    @property
    def contenu(self):
        """HTML ou src de l'image.
        """
        if not self.image and not self.integration:
            """Si l'utilisateur vide tous les champs image et intégration
            on supprime."""
            self.delete()
            return
        return self.integration or self.image
    
    @property    
    def type_media(self):
        """Type du média.
           :retourne: soundcloud, embeded ou imaged  
        """
        if self.integration and 'soundcloud.com' in self.video.lower():
            return u"soundcloud"
        elif self.integration:
            return u"embeded"
        else:
            return u"image"
        
    @property
    def miniature(self):
        """Si image retourne l'image.
           Si vidéo retourne une miniature si elle existe.
        """
        if self.image:
            return self.image
        if self.thumbnail_url:
            return self.thumbnail_url
        return False
                 
    def save(self, *args, **kwargs):
        if self.video != self.old_url and len(self.video) > 0:
            url=""
            scheme, domain, path, params, query, fragment = urlparse(self.video)
            if "dailymotion.com" in domain:
                url = "http://www.dailymotion.com/services/oembed?format=json&%s" % urllib.urlencode({"url": self.video})
            elif "youtube.com" in domain:
                url = "http://www.youtube.com/oembed?format=json&%s" % urllib.urlencode({"url": self.video})
            elif "vimeo.com" in domain:
                url = "http://vimeo.com/api/oembed.json?%s" % urllib.urlencode({"url": self.video})
            elif "soundcloud.com" in domain:
                url = "http://soundcloud.com/oembed?format=json&%s" % urllib.urlencode({"url": self.video}) 
                
            headers = {'User-Agent':  'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
            req = urllib2.Request(url, None, headers)
            obj = simplejson.loads(urllib2.urlopen(req).read())
            self.integration = obj.get("html", None)
            
             
            image_url = obj.get("thumbnail_url", None)
            if image_url:
                """Si l'endpoint ne fournie pas de miniature, on ne stocke rien."""
                name = urlparse(image_url)[2].split('/')[-1]            
                file = urllib.urlopen(image_url)
                img = Image.open(cStringIO.StringIO(file.read()))
                img.save('/tmp/%s' % name)
                self.thumbnail_url = File(open('/tmp/%s' % name))
            
            self.titre = obj.get("title", None)
        self.old_url = self.video        
        super(ContenuMediaAbstract, self).save(*args, **kwargs)
        

class Categorie(models.Model):
    """Catégorie du contenu de la médiathèque."""
    name = models.CharField(u'Catégorie', max_length=150)
    slug = AutoSlugField(populate_from='name', unique=True)
    image_principale = models.ImageField(upload_to='uploads/', null=True, blank=True)
    date_creation = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    def __unicode__(self):
        return self.name
    
    @models.permalink
    def get_absolute_url(self):
        return ('mediatheque:categorie_details', [self.slug])
    
    def images(self):
        """Retourne les images correspondantes à cette catégorie."""
        return Mediatheque.images.filter(categorie=self)
    
    def videos(self):
        """Retourne les vidéos correspondantes à cette catégorie."""
        return Mediatheque.videos.filter(categorie=self)
    
    def embed(self):
        """Retourne tout contenu insérable(iframe, embed) correspondantes à cette catégorie."""
        return Mediatheque.embed.filter(categorie=self)
    
    def get_absolute_imagep_url(self):
        return '%s%s' % (settings.MEDIA_URL, self.image_principale)
     
            
class Mediatheque(ContenuMediaAbstract):
    categorie = models.ForeignKey(Categorie, null=True, blank=True)
    