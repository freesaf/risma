from django.contrib import admin
from models import Categorie, Mediatheque

class MediathequeInline(admin.StackedInline):
    model = Mediatheque
    exclude = ('integration',)
    extra = 1


class CategorieAdmin(admin.ModelAdmin):
    inlines = [MediathequeInline,]
admin.site.register(Categorie, CategorieAdmin)