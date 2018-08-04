#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 19:28:10 2018

@author: larrylaw
"""

import scrapy

class TimetableSpider(scrapy.Spider):
    name = "timetable"
    start_urls = ['https://myaces.nus.edu.sg/cors/jsp/report/ModuleInfoListing.jsp']

    def parse(self, response):
        #follow link to details
        detailed_module_xpath = response.xpath("//table[@class='tableframe']/tr[position()>1]/td[2]/div/a/@href").extract()
        for href in response.xpath(detailed_module_xpath).extract():
            next_url = "https://myaces.nus.edu.sg/cors/jsp/report/"+href
            yield scrapy.Request(next_url, callback = self.parse_detailed)
    
    def parse_detailed(self, response):
        yield {
                "Module Code": response.xpath("normalize-space(//div[text()='Module Code :']/../../td[2])").extract()
                }
        