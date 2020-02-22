#v1_autoscheduler.py

#This software automatically schedules a person's time based on the number of tasks they need to do and their priorities. The software also tries to minimize the average amount of time before an assignment is due that the assignment is done, and asks the user to check in to rate how confident they are about an assignment.

#!/usr/bin/python3

###INCLUDE

import calendar
import importlib        #enable file import
from datetime import date

from modules import modules

###FUNCTIONS###
'''
def printTodayCal():
    todaycal = calendar.TextCalendar(calendar.monday)
    return

def printLine(num):
    print(num*"_")
    return

def printToday():
    today = date.today()
    print("Today's current date is -", today)
    return

def printDayCal(): 
    printLine(36)
    printToday()        #print the day's identifier
    printLine(36)
    for hour in range(24):      #for each hour up to 24, 
        print(str(hour),":00")      #print each hour's name in military format
    return
'''


###MAIN###

printDayCal()

