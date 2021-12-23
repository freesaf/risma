#-*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from models import News

class NewsForm(forms.ModelForm):
    contenu = forms.CharField(widget=CKEditorWidget(), required=False)
    class Meta:
        model = News
        
class NewsAdmin(admin.ModelAdmin):
    form = NewsForm
    list_display = ('__unicode__', 'type')
    list_filter = ('type',)
    
admin.site.register(News, NewsAdmin)