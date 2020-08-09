import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import urllib.parse
import threading


class TestSpider(CrawlSpider):
    name = "test"
    allowed_domains = ["cerve.co"]
    start_urls = ["https://cerve.co"]
    rules = [Rule(LinkExtractor(allow=['.*'], tags='a',
                                attrs='href'), callback='parse_item', follow=True)]

    def parse_item(self, response):
        alllinks = response.css('a::attr(href)').getall()
        self.logger.warning(
            "[ -------- "+response.url+" ------- ]")
        # for link in alllinks:
        #     link = response.urljoin(link)
        #     yield {
        #         'page': urllib.parse.unquote(response.url),
        #         'links': urllib.parse.unquote(link),
        #         'number of links': len(alllinks),
        #         'status': response.status
        #     }
