from classytags.core import Tag, Options
from classytags.arguments import Argument
from django import template
from gallerie.models import Gallerie, Photo
from django.template import loader, Context

register = template.Library()

class Carousel(Tag):
    name = 'carousel'
    options = Options(
        Argument('slug'),
        Argument('div_id'),
        Argument('taille', default="300x300", required=False, resolve=False),
        Argument('template_id', default="carousel_1", required=False, resolve=False)
    )
    
    def render_tag(self, context, slug, div_id, taille, template_id):
        photos = Photo.objects.filter(gallerie__slug=slug)
        variables = Context({"photos": photos, "taille": taille, "div_id": div_id})
        return loader.get_template('gallerie/%s.html' % template_id).render(variables)
    
register.tag(Carousel)

