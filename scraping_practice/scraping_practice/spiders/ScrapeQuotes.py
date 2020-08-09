import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class ScrapeQuotesSpider(CrawlSpider):
    name = 'ScrapeQuotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    rules = (
        Rule(LinkExtractor(
            restrict_xpaths="//li[@class='next']"), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        self.logger.info("Scraped url: "+response.url)
