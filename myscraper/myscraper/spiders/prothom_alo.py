import scrapy


class ProthomAloSpider(scrapy.Spider):
    name = 'prothom_alo'
    allowed_domains = ['prothomalo.com']
    start_urls = ['https://www.prothomalo.com/']

    def parse(self, response):
        pass
