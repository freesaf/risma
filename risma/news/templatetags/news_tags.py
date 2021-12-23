from classytags.core import Tag, Options
from classytags.arguments import Argument
from classytags.helpers import InclusionTag
from django import template
from news.models import News

register = template.Library()

class LatestNews(InclusionTag):
    name = 'latest_news'
    options = Options(
        Argument('count', required=False, resolve=False),
    )
    template = 'news/latest_news.html'
    
    def get_context(self, context, count):
        news = News.objects.all()[:count]
        return {"news": news}        
register.tag(LatestNews)


class DynamicNews(LatestNews):
    name = 'dynamic_news'
    template = 'news/dynamic_news.html'
register.tag(DynamicNews)
