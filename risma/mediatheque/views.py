#-*- coding: utf-8 -*-
from annoying.decorators import render_to
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from models import Mediatheque, Categorie

@render_to('mediatheque/image_list.html')
def image_list(request, slug=None):
    """Retourne l'ensemble des images de la médiathèque.
       Si ``slug`` est renseigné, renvoit les images de la catégorie qui y correspond. 
    """
    images = Mediatheque.images.all()
    if slug:
        images = images.filter(categorie__slug=slug)
    return {'images': images}


@render_to('mediatheque/video_list.html')
def video_list(request, slug=None):
    """Même chose que image_list."""
    images = Mediatheque.embed.all()
    if slug:
        images = images.filter(categorie__slug=slug)
    return {'images': images}


@render_to('mediatheque/categorie_list.html')
def categorie_list(request):
    """Liste des catégories non-vides."""
    return {"categories": Categorie.objects.filter(id__in=Mediatheque.objects.values('categorie').distinct())}


@render_to('mediatheque/image_categories_list.html')
def image_categories_list(request):
    categories = [cat for cat in Categorie.objects.all() if cat.images().exists()]
    return locals()


@render_to('mediatheque/categorie_details.html')
def categorie_details(request, slug):
    """Détails d'une catégorie."""
    categorie=get_object_or_404(Categorie, slug=slug)  
    categorie.image_principale = categorie.get_absolute_imagep_url() 
    image_principale=categorie.image_principale
    return locals()


def last_cat_media_list(request, type="image"):
    """retourne les vidéos ou les photos de la dernière catégorie 
    (classé par nom).
    @param type: reçoit `image` ou `video` pour définir quelle vue utiliser.
    """
      
    categories = Categorie.objects.order_by('-name')
    try:
        cat = categories[0]
    except IndexError:
        return categorie_list(request)
    
    if type == 'video':
        return HttpResponseRedirect(reverse('mediatheque:video_list', kwargs={'slug': cat.slug}))
    else:
        return HttpResponseRedirect(reverse('mediatheque:image_list', kwargs={'slug': cat.slug}))