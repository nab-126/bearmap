from scrapy import Spider
from scrapy.selector import Selector

from stack.items import StackItem

class StackSpider(Spider):
    name = "class-ie"
    allowed_domains = ["guide.berkeley.edu/courses/compsci/"]
    start_urls = [
        "http://guide.berkeley.edu/courses/compsci/",
    ]

    def parse(self, response):
        #//*[@id="courseinventorycontainer"]/div/div[2]
        # questions = Selector(response).xpath('//*[@id="courseinventorycontainer"]/div/div[2]')
        questions = Selector(response).xpath('//div[@class="courseblock"]/button/h3')
        #questions = Selector(response).xpath('//div[@class="summary"]/h3')

        print(len(questions))
        print('yo')
        for question in questions:
            item = StackItem()
            item['code'] = question.xpath(
                'span[@class="code"]/text()').extract()[0]
            yield item