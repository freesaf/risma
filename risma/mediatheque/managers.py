#-*- coding: utf-8 -*-
from django.db.models import Manager, Q 

class ImageManager(Manager):
    def get_query_set(self):
        """Retourne les médias de type image."""
        return super(ImageManager, self).get_query_set(
                        ).filter(image__contains="/",)
                        

class EmbededManager(Manager):
    def get_query_set(self):
        """Retourne les médias de type embed(vidéo/audio)."""
        return super(EmbededManager, self).get_query_set(
                        ).exclude(image__contains="/",)
                        

class VideoManager(Manager):
    def get_query_set(self):
        """Retourne les médias de type embed(vidéo/audio)."""
        return super(VideoManager, self).get_query_set(
                        ).exclude(Q(image__contains="/") | Q(video__contains="soundcloud.com"))