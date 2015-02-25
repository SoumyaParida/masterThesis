from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from craiglist_sample.items import CraiglistSampleItem

class MySpider(BaseSpider):
	name="craig"
	allowed_domains =["wikipedia.org"]
	start_urls=["https://www.wikipedia.org/"]

	def parse(self,response):
		hxs=HtmlXPathSelector(response)
		titles=hxs.select("//p")
		items =[]
		for titles in titles:
			items=CraiglistSampleItem()
			items["title"]=titles.select("a/text()").extract()
			items["ink"]=titles.select("a/@href").extract()
			items.append(items)
		return items