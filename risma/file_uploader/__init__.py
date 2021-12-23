#-*- coding: utf-8 -*-
"""File Uploader
   -------------

   Afin d'éviter à avoir à modifier des fichiers régulièrement, et de passer à chaque fois par le FTP. 
   Ce module a été créé pour permettre au client de mettre à jour ses fichires lui-même depuis l'admin
   l'utilisation se fait avec des templatetags::
       {% load fichier_tags %}
       {% fichier <id_fichier> %}


   .. note:: Vérifier après le déploiement, que le compte d'accès au panel d'admin fournit au client, n'a le droit que de modifier les fichiers qui existent déjà. Donc pas de droits d'ajout ou de suppression.
   
   .. warning:: le dossier dans lequel l'upload va avoir lieu *normalement uploadedfiles* **ne doit pas** être accessible par le user ``www-data``

"""