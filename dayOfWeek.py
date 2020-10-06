import re #regular expression
import calendar
import datetime


def processDate(userInput):
    userInput = re.sub(r"/"," ",userInput)
    userInput = re.sub(r"-"," ",userInput)
    
    return userInput


userInput = str(input("enter date : "))
date = processDate(userInput)
print("Day On : "+userInput)