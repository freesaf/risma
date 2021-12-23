#-*- coding: utf-8 -*-
from django import forms
from models import CV

class RecrutementForm(forms.ModelForm):
    class Meta:
        model = CV