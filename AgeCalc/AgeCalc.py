# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 17:36:50 2020

@author: Zachery Van Es
"""
import datetime
import math

def ageCalc():
    currentTime = datetime.datetime.now()
    x = True
    while x == True:
        birthday = input("Enter brithday(mm/dd/yyyy): ")
        if len(birthday.split("/")) == 3 :
            month, day, year = birthday.split("/")
            x = False
        else:
            print("Incorrect Input, Try again.")
    
    birthdayTime = datetime.datetime(int(year), int(month), int(day))    
    YearDifference = currentTime - birthdayTime
    yourAge = math.floor(YearDifference.days / 365.25)
    
    Output = "You are {} years old"
    print(Output.format(yourAge))
ageCalc()