# Web Crawler to crawl the National Interagency Fire Center's Statistics

import scrapy
import io
import re
from scrapy.item import Item


class NIFC_Spider(scrapy.Spider): 
    name = 'wildfireSpider'
    
    def start_requests(self): 
    	# First, scraping the wildfires larger than 100,000 acres
        urls = [
        'https://www.nifc.gov/fireInfo/fireInfo_stats_lgFires.html' ]
        for url in urls: 
        	yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
    	page = response.url.split("/")[-2]
    	filename = 'wildfireStats-%s.html' % page
    	with open(filename, 'wb') as f: 
    		f.write(response.body)
    	self.log('Saved file %s' % filename)
    	
                

