# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 18:14:42 2020

@author: Zachery Van Es
"""

def fizzBuzz():
    for x in range(1,101):
        Fizz = (x%3 == 0)
        Buzz = (x%5 == 0)
        if Fizz and Buzz:
            print("Fizz Buzz")
        elif Fizz:
            print("Fizz")
        elif Buzz:
            print("Buzz")
        else:
            print(x)
fizzBuzz()