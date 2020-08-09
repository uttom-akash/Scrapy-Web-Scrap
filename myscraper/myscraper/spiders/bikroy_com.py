# import scrapy
# import json
# # https://bikroy.com/en/users/login?action=login&redirect-url=/


# class BikroyComSpider(scrapy.Spider):
#     name = 'bikroy_com'
#     # allowed_domains = ['bikroy.com']
#     start_urls = [
#         'https://bikroy.com/en/users/login?action=undefined&redirect-url=/']

#     def parse(self, response):
#         self.logger.info("---------- : "+response.url)
#         yield {"resp": response.selector.xpath("//input")}
#         yield scrapy.Request(response, ,body=json.dumps({"session": {"email": "i.akash.se@gmail.com", "password": "akaashian"}}), callback=self.parse_after_login)

#     def parse_after_login(self, response):
#         yield {"loggedin ": response.selector.xpath("//input").getall()}
#     #     yield scrapy.Request("https://bikroy.com/en/my/dashboard", callback=self.parse_dashboard)

#     # def parse_dashboard(self, response):
#     #     yield {"Info ": response.selector.xpath("//h3/text()").getall()}
