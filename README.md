# AutomaticTimetableGenerator
Automatic Timetable Generator

## Issue
Time and labour intensive to go through all timetable permutations

## Solution
Automatic timetable generator that sorts timetable based on **least wasted time** (independent variable)

Assert

1. Meal Times
    1. Lunch: 11-12, 12-1, 1-2
    2. Dinner: 5-6, 6-7, 7-8
2. Start/End @ Utown
3. Exam Time does not coincide

Dependent Variables
1. Minimise travelling

Method| +| -
:---|:---|:---
Faculty breakdown by Google maps| - Fast: no need to learn any API <br /> - Stores permutations of the distance between faculty| - Not accurate (but does it really matter when put into perspective of other DVs?)
Google Maps Routes API| - Exact Distance <br /> - What if I can somehow store the data? (For loop through all permutations, calculating distance between all of them)| - Costly To Scale (data not stored > Every check = request to google -> $$) each <br /> - Time needed to learn API 
Grid breakdown in NUS Maps| - Finer breakdown of distance | - Problem w/ computer vision of what's inside the grid

2. Time wasted travelling between lectures if <1 hour (excluding lunch and time spent travelling)

## Data Scraping
Data Scraped| URL
:---|:---
Following link to Module Detailed Information| https://myaces.nus.edu.sg/cors/jsp/report/ModuleInfoListing.jsp|
Module Code, Module Title, Exam Date, Module Workload (to identify no. of lessons each), Lecture Time Table (Lec/Sec), Tutorial Time Table (Tut/Lab/Rec)| https://myaces.nus.edu.sg/cors/jsp/report/ModuleDetailedInfo.jsp?acad_y=2018/2019&sem_c=1&mod_c=ACC1002#TutorialTimeTable
Distance between faculties| 

Faculty|Address
:---|:---
UTown|"2 College Avenue West 01"
SoC|"Singapore 117417"
FASS|"Singapore 117570"
Engin|"Singapore 117575"
Biz|"Singapore 119245"
Science|"Singapore 117546"
Music|"Singapore 117485" 
Design_and_Environ|"Singapore 117566"
#Law|"Singapore 259776" 
#Dentistry|"Singapore 119083"
#Medicine_and_Nursing|"Singapore 119228"


