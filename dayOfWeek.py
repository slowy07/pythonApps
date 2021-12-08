import re  # regular expression
import calendar
import datetime


def processDate(userInput):
    userInput = re.sub(r"/", " ", userInput)
    userInput = re.sub(r"-", " ", userInput)

    return userInput


def findDay(date):
    born = datetime.datetime.strptime(date, "%d %m %Y").weekday()
    return calendar.day_name[born]


userInput = str(input("enter date : "))
date = processDate(userInput)
print("Day On : " + userInput + " is " + findDay(date))
