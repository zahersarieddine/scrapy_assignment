import scrapy
import tldextract

class UsvInvestorsSpider(scrapy.Spider):

    name = "usv"
    status_cat="current"
    allowed_domains = ['www.usv.com', ]

    def start_requests(self):
        urls = [f'https://www.usv.com/companies/?status-cat={self.status_cat}',]
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse) 

    def parse(self, response):
        domains = list(filter(lambda domain: domain != 'usv.com', list(map( lambda url : tldextract.extract(url).registered_domain , \
                        response.xpath("//div[@class='m__list-row ']").css('a').xpath('@href').extract()))))
        print(domains)
        yield {'domains': domains}
        