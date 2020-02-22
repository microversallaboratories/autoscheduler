#modules.py for modules library

###FUNCTIONS###

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
