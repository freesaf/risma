#-*- coding: utf-8 -*-
from django.db import models
from autoslug import AutoSlugField

TYPE_NEWS_CHOICES = (
    ('texte', 'Texte uniquement'),
    ('texte_image', 'Texte et image'),
    ('image_image', '2 Images')
)

class News(models.Model):
    titre = models.CharField(max_length=250) 
    contenu = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="photos", null=True, blank=True)
    image2 = models.ImageField(upload_to="photos", null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    favori = models.BooleanField(default=False) 
    slug = AutoSlugField(populate_from='titre', unique=True)
    type = models.CharField(max_length=20, null=True, blank=True, choices=TYPE_NEWS_CHOICES, default='texte')
   
    def __unicode__(self):
        return self.titre
    
    @models.permalink
    def get_absolute_url(self):
        return ("news_details", [self.slug])
        
    class Meta:
        verbose_name_plural = "News"
        
                
        