# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 19:03:12 2020

@author: Zachery Van Es
"""

def tempConvert():
    x = input("Enter temperture(C/F)\n")
    if len(x.split(" ")) == 2 :
        y, z = x.split(" ")
        temp = float(y)
        tempType = z.upper()
        if tempType == "C":
            temp = ((9.0/5.0*temp)+32.0)
            tempType = "F"
        else:
            temp = (5.0/9.0*(temp-32.0))
            tempType = "C"
        newTemp = "Your new temp is {:.2f} {}"
        print(newTemp.format(temp, tempType))
    else:
        print("Input incorrect")
tempConvert()