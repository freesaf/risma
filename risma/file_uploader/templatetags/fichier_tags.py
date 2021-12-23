from annoying.functions import get_object_or_None
from classytags.core import Tag, Options
from classytags.arguments import Argument
from django import template
from django.template import loader, Context

from file_uploader.models import Fichier

register = template.Library()

class FichierTag(Tag):
    name = 'fichier'
    options = Options(
        Argument('id'),
    )
    
    def render_tag(self, context, id):
        fichier = get_object_or_None(Fichier, pk=id)
        variables = Context({"fichier": fichier})
        return loader.get_template('file_uploader/lien.html').render(variables)
register.tag(FichierTag)


@register.inclusion_tag('include/dummy.html')
def get_file_by_cat(categorie=None, template_name='file_uploader/tags/fichier_categorie.html'):
    fichiers = Fichier.objects.filter(categorie__nom=categorie).order_by('-id')
    return locals()