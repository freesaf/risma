#-*- coding: utf-8 -*-
#from modeltranslation.admin import TranslationStackedInline, TranslationAdmin
from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget

from models import  CommuniquePresse , Diffusion
    

#class CommuniquePresseAdmin(TranslationAdmin):
class CommuniquePresseForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget(), required=False)
    class Meta:
        model = CommuniquePresse
      
class CommuniquePresseAdmin(admin.ModelAdmin):
    form = CommuniquePresseForm
    search_fields = ('titre',)
    list_display = ('titre', 'date',)
    
admin.site.register(CommuniquePresse, CommuniquePresseAdmin)


admin.site.register(Diffusion)
