#-*- coding: utf-8 -*-
from django import forms
from models import Contact
from django.utils.translation import ugettext as _


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact