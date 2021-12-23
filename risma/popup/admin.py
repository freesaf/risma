#-*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget

from models import Popup, Categorie

class PopupForm(forms.ModelForm):
    texte = forms.CharField(widget=CKEditorWidget(), required=False)
    class Meta:
        model = Popup
      
class PopupAdmin(admin.ModelAdmin):
    form = PopupForm
    list_display = ('titre','texte')
    
    
admin.site.register(Popup, PopupAdmin)

admin.site.register(Categorie)