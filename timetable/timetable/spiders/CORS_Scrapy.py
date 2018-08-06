#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 19:28:10 2018

@author: larrylaw
"""

import scrapy
from scrapy.crawler import CrawlerProcess

class TimetableSpider(scrapy.Spider):
    name = "timetable"
    start_urls = ['https://myaces.nus.edu.sg/cors/jsp/report/ModuleInfoListing.jsp']

    def parse(self, response):
        #follow link to details
        for href in response.xpath("//table[@class='tableframe']/tr[position()>1]/td[2]/div/a/@href").extract():
            next_url = "https://myaces.nus.edu.sg/cors/jsp/report/"+href #correct
            yield scrapy.Request(next_url, callback = self.parse_detailed)
    
    def parse_detailed(self, response):
        return {
                "Module Code": response.xpath("normalize-space(//div[text()='Module Code :']/../../td[2])").extract()
                }
        #Definitely correct

process = CrawlerProcess()
process.crawl(TimetableSpider)
process.start()

https://myaces.nus.edu.sg/cors/jsp/report/ModuleDetailedInfo.jsp?acad_y=2018/2019&sem_c=1&mod_c=ACC1002