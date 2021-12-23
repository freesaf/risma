#-*- coding: utf-8 -*-
"""
Utilisé généralement pour la gestion de news basiques (Image(s) + Texte), citations... Ou tout contenu du genre.
Il permet aussi la gestion dynamique du rendu selon le type de la news. Les options disponibles actuellement sont : 

* Texte seulement
* Texte + Image
* 2 Images

Pour un usage basique du module il suffit de l'appeller dans le template comme suit::

    {% load news_tags %}    
    {% latest_news [nombre_news_a_afficher] %}

Ou pour une gestion dynamique du rendu::

    {% dynamic_news [nombre_news_a_afficher] %}
"""