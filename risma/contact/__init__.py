#-*- coding: utf-8 -*-
"""Ce module permet d'afficher un formulaire de contact, d'envoyer un e-mail au propriétaire du site et 
   d'enregister tout les message dans la base de données, au cas où l'email n'est pas arrivé à destination ou considéré comme spam. 

   Pour Ajouter ou modifier des champs dans models.py réferez-vous à la documentation officielle de django https://docs.djangoproject.com/en/dev/ref/models/fields/

   .. warning:: N'oubliez pas de lancer la migrations après :ref:`migration_modele`

   N'oubliez pas aussi de modifiez les variables global pour l'envoi d'email dans le fichier settings.py ::

    EMAIL = "sender@wbc.ma" # l'email du client (surquel il souhaite recevoir ces messages)
    EMAIL_HOST = 'localhost' 
    EMAIL_HOST_USER = 'sender@wbc.ma' # Compte pour s'authenfier sur le serveur smtp, les emails seront envoyé à partir de ce compte
    EMAIL_HOST_PASSWORD = 'pass'
    EMAIL_PORT = 25
    
   .. note:: Modifier les memes variables dans le local_settings.py pour faire des tests.

   .. warning:: Si vous effectuer des modifs sur le modèle vous devez remodifier la template contact/email_body.txt avec les bonnes propriétés
"""