#-*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.sites.models import Site
from django.template import Library
from django.conf import settings

register = Library()


@register.inclusion_tag('include/dummy.html')
def share_buttons(social_networks="all",  title=None, url=None, description=None, image=None, theme="large",template_name='social_sharing/tags/sharing.html'):
    #Séparer les valeurs si plusieurs, sinon vaut all
    social_networks = social_networks.split(",") if "," in social_networks else social_networks
    show_button = lambda x : True if x in social_networks else False
    
    #Choix des services à afficher
    if social_networks == 'all':
        tw = fb_like = fb_share = gplus = email = True
    else:
        tw = show_button('tw')
        fb_like = show_button('fb_like')
        fb_share = show_button('fb_share')
        gplus = show_button('gplus')
        email = show_button('email')
    
    title = str(title)   
    url = settings.SITE_URL + str(url)
    description = description
    image = settings.SITE_URL + str(image)
    theme = theme
    
    return locals()


@register.inclusion_tag('include/dummy.html')
def share_buttons_(social_networks="all", object=None, theme="large", template_name='social_sharing/tags/sharing.html'):
    #Séparer les valeurs si plusieurs, sinon vaut all
    social_networks = social_networks.split(",") if "," in social_networks else social_networks
    show_button = lambda x : True if x in social_networks else False
    
    #Choix des services à afficher
    if social_networks == 'all':
        tw = fb_like = fb_share = gplus = email = True
    else:
        tw = show_button('tw')
        fb_like = show_button('fb_like')
        fb_share = show_button('fb_share')
        gplus = show_button('gplus')
        email = show_button('email')
        
    title = str(object.title)   
    url = settings.SITE_URL + object.get_absolute_url()
    if hasattr(object, 'description'):
        description = object.description
    if hasattr(object, 'social'):
        image = settings.SITE_URL + object.social['image']
    else:
        if hasattr(object, 'image') and object.image:
            image = settings.SITE_URL + object.image.url
    theme = theme
    return locals()
    

