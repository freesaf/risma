#-*- coding: utf-8 -*-
from django.template import Library
from mediatheque.models import Categorie, Mediatheque

register = Library()

@register.inclusion_tag('include/dummy.html')
def categories_mediatheque(current_cat=None, template_name='mediatheque/tags/categories_menu.html'):
    """
    Affiche la liste des catégories de la mediathèque.    
    Utilisation::    
        {% categories_mediatheque [categorie_actuelle] [template_name] %}    
    .. note:: En cas d'utilisation de ce templatetag comme menu, ``categorie_actuelle`` sert juste à passer la catégorie active.    
    """
    categories = Categorie.objects.filter(id__in=Mediatheque.objects.values('categorie').distinct())     
    return {"categories": categories}


@register.inclusion_tag('include/dummy.html')
def mediatheque_get_latest_categories(count=5, template_name='mediatheque/tags/latest_categories.html'):
    """
        Retourne les dernières catégories de la mediathèque        
        Utilisation::    
            {% mediatheque_get_latest_categories [count] [template_name] %}            
        .. note:: Si pas renseigné, le count est égal par défaut à 5.
         
    """
    try:
        categories = Categorie.objects.order_by('-date_creation')[:count]
    except IndexError:
        categories = []
        
    return locals()


@register.inclusion_tag('include/dummy.html')
def mediatheque_get_latest_image(count=1, template_name='mediatheque/tags/latest_image.html'):
    categorie = Categorie.objects.latest('date_creation')
    image = categorie.image_principale
    return locals()
