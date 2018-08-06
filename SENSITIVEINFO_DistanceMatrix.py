#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 17:37:50 2018

@author: larrylaw
"""
def Convert_Whitespace_String(input_string):
    """
    Converts whitespace to "+"
    """
    new_string = ""
    for char in input_string:
        if char == " ":
            char = "+"
        new_string = new_string+char
    return new_string

def Distance_Matrix_Origins(input_list):
    """
    Input faculty list
    Returns Origin string parameter of Distance Matrix
    """
    origins = "origins="
    count = 1
    for elt in input_list:
        if count != len(input_list):
            origins = origins+Convert_Whitespace_String(elt)+"|"            
        else:
            origins = origins+Convert_Whitespace_String(elt)
        count += 1
    return origins

def Distance_Matrix_Destinations(input_list):
    """
    Input faculty list
    Returns Destination string parameter of Distance Matrix
    """
    destinations = "destinations="
    count = 1
    for elt in input_list:
        if count != len(input_list):
            destinations = destinations+Convert_Whitespace_String(elt)+"|"            
        else:
            destinations = destinations+Convert_Whitespace_String(elt)
        count += 1
    return destinations

def Distance_Matrix_URL(Faculty, key, mode = "walking", language = "en"):
    """
    Input: List of Faculty, key, "walking" is default mode, "en" is default language
    Returns Google Maps Distance Matrix URL
    """
    intro = "https://maps.googleapis.com/maps/api/distancematrix/json?"
    origins = Distance_Matrix_Origins(Faculty)
    destinations = Distance_Matrix_Destinations(Faculty)
    mode = "mode="+mode
    language = "language="+language
    key = "key="+key
    URL = intro+origins+"&"+destinations+"&"+mode+"&"+language+"&"+key      
    return URL

UTown="2 College Avenue West 01"
SoC="Singapore 117417"
FASS="Singapore 117570"
Engin="Singapore 117575"
Biz="Singapore 119245"
Science="Singapore 117546"
Music="Singapore 117485" 
Design_and_Environ="Singapore 117566"
#Bukit Timah Campus
#Law="Singapore 259776" 
#Dentistry="Singapore 119083"
#Medicine_and_Nursing="Singapore 119228"
Faculties = [UTown, SoC, FASS, 
             Engin, Biz, Science, 
             Music, Design_and_Environ]
Distance_Matrix_URL(Faculties, "AIzaSyBAb1pn5LaZFUdqjQphSgAARS9FxOp46jw")


