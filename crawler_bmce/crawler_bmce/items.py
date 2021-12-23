# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class CrawlerBmceItem(Item):
    # define the fields for your item here like:
    # name = Field()
    last_quote = Field()
    currency= Field()
    variation= Field()
    curseur= Field()
    date= Field()
    isin= Field()
    market_center= Field()

