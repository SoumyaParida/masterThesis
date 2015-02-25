# Scrapy settings for craiglist_sample project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'craiglist_sample'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['craiglist_sample.spiders']
NEWSPIDER_MODULE = 'craiglist_sample.spiders'
DEFAULT_ITEM_CLASS = 'craiglist_sample.items.CraiglistSampleItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

