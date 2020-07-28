from scrapy import Spider
from scrapy.selector import Selector

from stack.items import StackItemMajor

# class StackSpider(Spider):
#     name = "major_spider"
#     allowed_domains = ["http://guide.berkeley.edu/courses/stat/"]
#     start_urls = [
#         "http://guide.berkeley.edu/courses/stat/",
#     ]

#     def parse(self, response):
#         questions = Selector(response).xpath('//div[@class="courseblock"]')
#         # questions = Selector(response).xpath('//div[@class="courseblock"]/button/h3')
#         for question in questions:
#             item = StackItemMajor()
#             item['code'] = question.xpath(
#                 'button/h3/span[@class="code"]/text()').extract()[0].replace("\u00a0", " ")
#             # item['code'] = question.xpath('div[@class="course-section"]/')
#             item['prerequisites'] = question.xpath('div/div/div/p/a[@class="bubblelink code"]/text()').extract()
#             yield item