import scrapy
import tldextract
from urllib.parse import urljoin

from list_investors.items import ListInvestorsItem
class AnthemisInvestorsSpider(scrapy.Spider):

    name = "anthemis"

    def start_requests(self):
        urls = ['https://www.anthemis.com/invest/',]       
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)    
        
    
    def parse(self, response):
        # get all link elements that have are in div elements with class 'team-member' and then iterate over them to yield a separate 
        # request that will be handled by another parser
        investors = response.xpath("//*[contains(@class, 'team-member')]/a/@href").extract()
        for investor in investors:          
            url = urljoin(response.url, investor)          
            yield scrapy.Request(url, callback=self.parse_investor_page)      
                       
    def parse_investor_page(self, response):
        item = ListInvestorsItem()
        # some investor pages include 'website' label and others contain 'Website'. to allow both labels to pass the filter, translate the label to
        # lower case before comparing it  
        inv_url = response.xpath("//a[contains(translate(.,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz'),'website')]/@href").get()
        item['name'] = tldextract.extract(inv_url).registered_domain
        yield item
