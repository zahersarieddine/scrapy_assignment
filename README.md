# scrapy_assignment
This is a small scrapy projects with 2 spiders

Using python 3.9 and Scrapy create scrapers for VC investment portfolios. 

Input: Only needs to work for 2 VCs, each will require a different spider

1. One level scraper: https://www.usv.com/companies/?status-cat=current
2. Two level scraper: https://www.anthemis.com/invest/

Output: A list of active investment companies where each company is indicated by its web domain i.e. www1.x.com becomes x.com

## Excecution

### usv spider
scrapy crawl usv --nolog -a status_cat='current'

If status_cat is not specified then the spider will use the 'current' value by default. possible values are: all, current, acquired, public, inactive

### anthemis spider
scrapy crawl anthemis --nolog
