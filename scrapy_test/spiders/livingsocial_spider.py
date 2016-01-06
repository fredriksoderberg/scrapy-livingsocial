from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import XPathItemLoader
from scrapy.loader.processors import Join, MapCompose

from scrapy_test.items import LivingSocialDeal

class LivingSocialSpider(Spider):
    name = "livingsocial"
    allowed_domains = ["livingsocial.com"]
    start_urls = ["https://www.livingsocial.com/cities/15-san-fransisco"]
    
    deals_list_xpath = '//li[@dealid]'
    item_fields = {
        'title': './/span[@itemscope]/meta[@itemprop="name"]/@content',
        'link': './/a/@href',
        'location': './/a/div[@class="deal-details"]/p[@class="location"]/text()',
        'original_price': './/a/div[@class="deal-prices"]/div[@class="deal-strikethrough-price"]/div[@class="strikethrough-wrapper"]/text()',
        'price': './/a/div[@class="deal-prices"]/div[@class="deal-price"]/text()',
        'end_date': './/span[@itemscope]/meta[@itemprop="availabilityEnds"]/@content'
    }
    
    def parse(self, response):
        selector = Selector(response)
        
        for deal in selector.select(self.deals_list_xpath):
            loader = XPathItemLoader(LivingSocialDeal(), selector=deal)
            
            loader.default_input_processor = MapCompose(unicode.strip)
            loader.default_output_processor = Join()
            
            for field, xpath in self.item_fields.iteritems():
                loader.add_xpath(field, xpath)
            
            yield loader.load_item()