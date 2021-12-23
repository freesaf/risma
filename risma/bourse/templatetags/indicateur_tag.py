from classytags.core import Tag, Options
from classytags.arguments import Argument
from classytags.helpers import InclusionTag
from django import template
from risma.bourse.models import Indicator

register = template.Library()

class Indicateur(InclusionTag):
    options = Options(
        Argument('count', required=False, resolve=False),
    )

    def get_context(self, context, count=0):
        indicat_eur = Indicator.objects.all().order_by('-id')[:1]
        return {"indicateur": indicat_eur}
register.tag(Indicateur)


class Indicator_tag(Indicateur):
    name = 'indicateur'
    template = 'bourse/indicateur.html'
register.tag(Indicator_tag)




