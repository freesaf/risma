from crawler_bmce.items import CrawlerBmceItem
#from scrapy.utils.project import get_project_settings as Settings
import scrapy

class coursSpider(scrapy.Spider):

    name = 'cours'
    allowed_domains = ["bmcecapitalbourse.com"]
    domain_name= "bmcecapitalbourse.com"
    start_urls = ["http://www.bmcecapitalbourse.com/action.hts?menu=action_cours&id=1730672,102,608"]

    def parse(self, response):

        items = []
        item = CrawlerBmceItem()
        item["last_quote"] = response.xpath('//span[@id="LastQuote"]/text()')[0].extract()
        item["currency"] = response.xpath('//span[@id="Currency"]/text()')[0].extract()
        item["variation"] = response.xpath('//span[@id="Variation"]/text()')[0].extract()
        item["curseur"] = response.xpath('//img[@id="Curseur"]/@alt')[0].extract()
        item["date"]= response.xpath('//span[@id="Date"]/text()')[0].extract()
        item["isin"]= response.xpath('//span[@id="Isin"]/text()')[0].extract()
        item["market_center"]= response.xpath('//span[@id="MarketCenter"]/text()')[0].extract()
        items.append(item)
        #print items
        return items
