import scrapy
from scrapy.http import Request, FormRequest

#from scrapy.utils.project import get_project_settings as Settings
DATA_ROOT = "../risma/site_media/bmce/indicateur"

class indicateurSpider(scrapy.Spider):

    name = 'indicateur'
    allowed_domains = ["bmcecapitalbourse.com"]
    domain_name= "bmcecapitalbourse.com"
    start_urls = ["http://www.bmcecapitalbourse.com/action.hts?menu=action_histo&id=1730672,102,608"]

    def parse(self, response):

        liens = response.xpath('//a[@id="HandleTelecharge"]/@href').extract()
        print 'liens'
	print liens
	if liens:
            yield Request(url="http://www.bmcecapitalbourse.com%s" % liens[0],
                      callback=self.data_ll)

    def data_ll(self, response):
        filename = response.headers["Content-Disposition"].replace("inline; filename=", "")
        print 'filename'
	print filename
	open("%s/data/%s" % (DATA_ROOT, filename), "wb").write(response.body)

