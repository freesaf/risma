#-*- coding: utf-8 -*-
from modeltranslation.admin import TranslationStackedInline, TranslationAdmin
from contentadmin.admin import ImageContentInline, TextContentInline, PageAdmin
from contentadmin.models import Page, TextContent
from django.contrib import admin


from annuaire.models import EntreeAnnuaire
from file_uploader.models import Fichier
from gallerie.models import Gallerie, Photo
from mediatheque.admin import MediathequeInline
from mediatheque.models import Categorie as MediathequeCategorie
from news.admin import NewsAdmin
from news.models import News

 
class EntreeAnnuaireAdmin(TranslationAdmin):
    list_display = ('nom', 'adresse', 'ville', 'telephone', 'email')
admin.site.register(EntreeAnnuaire, EntreeAnnuaireAdmin)

####" PAGE !!!!!!!"


class TranslationFichierAdmin(TranslationAdmin):
    pass
admin.site.register(Fichier, TranslationFichierAdmin)



class PhotoInline(TranslationStackedInline):
    model = Photo
    extra = 2
    
class GallerieAdmin(TranslationAdmin):
    inlines = [PhotoInline]
    list_display = ("titre", "slug")
admin.site.register(Gallerie, GallerieAdmin)


class TranslationCategorieAdmin(TranslationAdmin):
    inlines = [MediathequeInline,]
admin.site.register(MediathequeCategorie, TranslationCategorieAdmin)


class TranslationNewsAdmin(NewsAdmin, TranslationAdmin):
    pass
admin.site.register(News, TranslationNewsAdmin)

