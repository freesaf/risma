#-*- coding: utf-8 -*-
from django.template.loader import render_to_string
from django.db.models.signals import pre_save, post_save
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

from models import CV


def recrutement_handler(sender, **kwargs):
    recrutement = kwargs['instance']
    titre = render_to_string('recrutement/email_titre.txt', 
                            {'recrutement': recrutement})
    body = render_to_string('recrutement/email_body.txt', 
                            {'recrutement': recrutement})
    
    
    email = EmailMultiAlternatives(titre, body, settings.EMAIL_HOST_USER, [settings.EMAIL]) 
    email.attach_alternative(body, "text/html")
    #email.attach_file(recrutement.cv.path)
    sent = email.send()

post_save.connect(recrutement_handler, sender=CV)
