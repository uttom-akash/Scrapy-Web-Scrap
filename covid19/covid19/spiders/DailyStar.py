import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re


class DailystarSpider(CrawlSpider):
    name = 'DailyStar'
    allowed_domains = ['thedailystar.net']
    start_urls = ['https://www.thedailystar.net/tags/coronavirus-bangadesh']

    rules = (
        Rule(LinkExtractor(allow=[".*tags/coronavirus-bangadesh.*"], allow_domains='thedailystar.net'),
             callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {
            'link': response.url
        }
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
