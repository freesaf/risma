from django.contrib import admin
from models import Gallerie, Photo

class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 2
    
class GallerieAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]
    list_display = ("titre", "slug")

admin.site.register(Gallerie, GallerieAdmin)