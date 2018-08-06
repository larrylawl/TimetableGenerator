#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 19:30:01 2018

@author: larrylaw
"""

import json

with open("/Users/larrylaw/Documents/CS/TimetableGenerator /NUS_Faculty_Distance_Matrix.json", "r") as file:
    data_distance_json = json.load(file)

data_distance = {}
Faculties = ("UTown", "SoC", "FASS", 
             "Engin", "Biz", "Science", 
             "Music", "Design_and_Environ")

for i, origin in enumerate(data_distance_json["rows"]):
    for j, destination in  enumerate(origin["elements"]):
        duration_dict = destination["duration"]
        duration_string = duration_dict["text"]
        data_distance["%s>%s" %(Faculties[i],Faculties[j])] = duration_string
        
with open("/Users/larrylaw/Documents/CS/TimetableGenerator /timetable/CORS_data.json") as file:
    cors_data = json.load(file)


