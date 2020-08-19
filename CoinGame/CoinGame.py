# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 17:01:58 2020

@author: Zachery Van Es
"""
import random
sequence = ["heads","tails"]


def headsOrTails():
    x = True
    
    while x == True:
        answer = input("Heads or tails?\n")
        coin = random.choice(sequence)
        
        print("The coin is "+coin)
        
        if coin == answer.lower():
            print("Good Job!")
        else:
            print("Better luck next time!")
            answer = input("Try again?(y/n)\n")
            if answer != "y":
                x = False
            
headsOrTails()