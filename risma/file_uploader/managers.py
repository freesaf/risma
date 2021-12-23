from django.db import models
from django.db.models import Q



class PublicationManager(models.Manager):
    """Manager to retrieve published authors"""

    def get_query_set(self):
        """Return published authors"""
        return super(PublicationManager, self).get_query_set()#.exclude(
                #Q(categorie__isnull=True) | Q(categorie__nom__contains="Dossiers de presse")
				#categorie__isnull=True
            #)

