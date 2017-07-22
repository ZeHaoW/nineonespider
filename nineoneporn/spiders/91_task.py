import scrapy
from scrapy import Selector

class NineoneSeedsSpider(scrapy.Spider):
    name = "91_task"
    start_urls = ["http://email.91dizhi.at.gmail.com.8h3.space/v.php?next=watch"]

    def parse(self, response):
        selector = Selector(response)
        content_list = selector.xpath("//div[@class='listchannel']")
        for content in content_list:
            content_url = content.xpath("a[@target='blank']/@href").extract()
            title = content.xpath("a/@title").extract()
            print content_url, title