from urllib.parse import urljoin
import scrapy

class AnthemisInvestorsSpider(scrapy.Spider):

    name = "anthemis"
    i = 0
    j = 0
    
    def start_requests(self):
        urls = ['https://www.anthemis.com/invest/',]       
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)   

    def parse(self, response):
        investors = response.xpath("//*[contains(@class, 'team-member')]/a/@href").extract()
        for investor in investors:          
            url = urljoin(response.url, investor)          
            yield scrapy.Request(url, callback=self.parse_investor_page)

    def parse_investor_page(self, response):
        if response.xpath("//a[contains(translate(.,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'website')]").get():
            self.i += 1
            inv = response.xpath("//a[contains(translate(.,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'website')]/@href").get().split('//')[1].split('/')[0].replace('www.', '') #.replace('/', '')
            print('{}: {}'.format(self.i, inv))
        else:
            self.j += 1
            print('-{} {}: {}'.format(self.j, 'missing website', response.xpath('//title/text()').get() ))
