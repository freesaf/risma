from ckeditor.widgets import CKEditorWidget

from django import forms
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


from models import *

"""
class ContenuInline(admin.StackedInline):
    #content = forms.CharField(widget=CKEditorWidget(config_name="flatpages"))
    model = Contenu
    extra = 1from django.template.defaultfilters import slugify
"""    
    
         
class FlatpageForm(forms.ModelForm):
    url = forms.RegexField(label=_("URL"), max_length=100, regex=r'^[-\w/]+$',
        help_text = _("Example: '/about/contact/'. Make sure to have leading and trailing slashes."),
        error_message = _("This value must contain only letters, numbers, underscores, dashes or slashes."))
    content = forms.CharField(widget=CKEditorWidget(), required=False)
    class Meta:
        model = FlatPage


class FlatPageAdmin(admin.ModelAdmin):
    form = FlatpageForm
    fieldsets = (
        (None, {'fields': ('url', 'title', 'categorie','mot_cle','ordre')}),
        (_('Advanced options'), {'fields': ('enable_comments', 'registration_required', 'template_name')}),#'classes': ('collapse',), 
        (_('Contenu'), {'fields': ('content','image','image_thumbnail')})
    )
    list_display = ('url', 'title', 'categorie')
    list_filter = ( 'enable_comments', 'registration_required', 'categorie')
    search_fields = ('url', 'title')
    
    #inlines = [ContenuInline,]
admin.site.register(FlatPage, FlatPageAdmin)

"""
class ContenuForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget(), required=False)
    class Meta:
        model = Contenu
      
class ContenuAdmin(admin.ModelAdmin):
    form = ContenuForm
    
admin.site.register(Contenu, ContenuAdmin)
"""


admin.site.register(Categorie)
