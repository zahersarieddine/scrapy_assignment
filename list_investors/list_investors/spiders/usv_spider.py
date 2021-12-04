import scrapy
from scrapy import Selector

class UsvInvestorsSpider(scrapy.Spider):

    name = "usv"
    status_cat="current"
    allowed_domains = ['www.usv.com', ]

    def start_requests(self):
        urls = [f'https://www.usv.com/companies/?status-cat={self.status_cat}',]
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse) 

    def parse(self, response):
        i = 0
        sel = Selector(response)
        divs = sel.xpath("//div[@class='m__list-row ']")

        for divx in divs:
            inv = divx.css('a').xpath('@href').get().split('//')[1].split('/')[0].replace('www.', '')
            if inv != 'usv.com':
                i += 1
                print('{}: {}'.format(i, inv))
