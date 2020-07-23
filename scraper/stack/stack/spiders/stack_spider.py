from scrapy import Spider

class StackSpider(Spider):
    name = "class-ie"
    allowed_domains = ["guide.berkeley.edu/courses/"]
    start_urls = [
        "http://guide.berkeley.edu/courses/",
    ]

    def parse(self, response):
        questions = Selector(response).xpath('//div[@class="summary"]/h3')

        for question in questions:
            item = StackItem()
            item['title'] = question.xpath(
                'a[@class="question-hyperlink"]/text()').extract()[0]
            item['url'] = question.xpath(
                'a[@class="question-hyperlink"]/@href').extract()[0]
            yield item