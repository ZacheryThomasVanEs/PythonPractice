# -*- coding: utf-8 -*-
import random

x = ["Tom","Bill","Logan","Robert","Sam","Garry","Zack","Jeff","George"]
y = ["Smith","White","Black","Wolf","Johnson","Williams","Brown","Jones"]

def namGenerator():
    lengthX = len(x)
    lengthY = len(y)
    z = "y"
    
    while z is "y":
        name1 = x[random.randrange(0, lengthX)]
        name2 = y[random.randrange(0, lengthY)]
        print(name1+" "+name2)
        z = input("Continue?(y/n): ")
    
namGenerator()


