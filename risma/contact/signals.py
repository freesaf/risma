#-*- coding: utf-8 -*-
from constance import config
from django.template.loader import render_to_string
from django.db.models.signals import pre_save, post_save
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

from models import Contact


def contact_handler(sender, **kwargs):
    contact = kwargs['instance']
    titre = render_to_string('contact/email_titre.txt', 
                            {'contact': contact})
    body = render_to_string('contact/email_body.html', 
                            {'contact': contact})
    email = EmailMultiAlternatives(titre, body, settings.EMAIL_HOST_USER, [config.EMAIL])
    email.attach_alternative(body, "text/html")
    sent = email.send()
    
post_save.connect(contact_handler, sender=Contact)
