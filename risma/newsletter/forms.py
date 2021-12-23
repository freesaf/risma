#-*- coding: utf-8 -*-
from django import forms
from models import Email

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Email
        
    def save(self, commit=True):
        """Si l'email n'existe pas déjà dans la base de données, on enregistre."""
        if not Email.objects.filter(email=self.cleaned_data['email']).exists():
            super(NewsletterForm, self).save(commit=commit)
