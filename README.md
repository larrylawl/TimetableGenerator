# AutomaticTimetableGenerator
Automatic Timetable Generator

## Issue
Time and labour intensive to go through all timetable permutations

## Solution
Automatic timetable generator that sorts timetable based on 
1. Maker's Schedule
    - Partitions timetable to three units: Morning, Noon (>= 4 hours), and Night
    - Rationale: Need large chunks of time to be productive
2. Manager's Schedule
    - Partitions timetable to 1 hour units
    - Rationale: Schedule of command
3. Off Campus Schedule
    - Minimal School days
    - Rationale: Time travelled to school; stricter version of Maker's Schedule
Source: http://www.paulgraham.com/makersschedule.html

Assert
1. Meal Times
    1. Lunch: 11-2
    2. Dinner: 5-8
2. Exam Time does not coincide
3. Start/End @ Utown
4. No 8 AM classes (?)

Extensions
1. Populate gym timings out (?)

Dependent Variables
1. Class timings
2. Minimise travelling

Method| +| -
:---|:---|:---
Faculty breakdown by Google maps| - Fast: no need to learn any API <br /> - Stores permutations of the distance between faculty| - Not accurate (but does it really matter when put into perspective of other DVs?)
Google Maps Routes API| - Exact Distance <br /> - What if I can somehow store the data? (For loop through all permutations, calculating distance between all of them)| - Costly To Scale (data not stored > Every check = request to google -> $$) each <br /> - Time needed to learn API 
Grid breakdown in NUS Maps| - Finer breakdown of distance | - Problem w/ computer vision of what's inside the grid

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
#Design_and_Environ|"Singapore 117566"
#Law|"Singapore 259776" 
#Dentistry|"Singapore 119083"
#Medicine_and_Nursing|"Singapore 119228"

## Pseudo Code
1. Method to initialise
    1. Arguments include: Mods, Timing (optional, if None, yield from database), Own commitments, Set timetable limit
2. Generate Timetable
    1. Mon - Fri
    2. Hourly partitioned based on user's timetable limit
3. Sort mods based on how limiting they are
    1. No. of options
    2. Spread across week
4. Magic Timetable
    1. Fix the most limiting mods
    2. Identify gaps in timetable to suit Maker's schedule
    3. Limiting mods go first

## Notes
1. If classes are the same, they MUST go together
2. Temp removed D&E for their lecture type/tutorial goes on the same timing, which will mess the algo up


