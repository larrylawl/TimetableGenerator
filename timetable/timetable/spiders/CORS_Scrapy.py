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
        for cycle in range:
                {
                "Module Code": response.xpath("normalize-space(//div[text()='Module Code :']/../../td[2])").extract(),
                "Module Title": response.xpath("//td[text()='Module Title :']/../td[2]/text").extract(),
                "Exam Date": response.xpath("normalize-space(//td[text()='Exam Date :']/../td[2]/text())").extract() 
                
                }
    def make_lecture_dict(lecture_list):
        """
        Input: List of lecture time table, unsorted by class
        Output: Dictionary of lecture time table, sorted by class
        """
        for row in range(int(len(lecture_list)/7)): #for each row in Lecture Time Table
            lecture_details["V"+str(row+1)] = {
                                                "Class": lecture_list[0+(7*row)],
                                                "Type": lecture_list[1+(7*row)],
                                                "Week Type": lecture_list[2+(7*row)]
                                                "Week Day": lecture_list[3+(7*row)]
                                                "Start": lecture_list[4+(7*row)]
                                                "End": lecture_list[5+(7*row)]
                                                "Room": lecture_list[6+(7*row)]
                                                }
                            
                            
                            
                
                                                
                
{"Class": lecture_list[0+(7*row)],
                       
                
                
                
                }
            
            
