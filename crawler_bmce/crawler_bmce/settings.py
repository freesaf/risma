# Scrapy settings for crawler_bmce project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'crawler_bmce'
# BOT_VERSION = '1.0'

SPIDER_MODULES = ['crawler_bmce.spiders']
NEWSPIDER_MODULE = 'crawler_bmce.spiders'
#USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

