# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 17:15:03 2020

@author: Zachery Van Es
"""
import random

if __name__ == "__main__":
    rpsChoicesMap = {0:"rock",1:"paper",2:"scissors"}
    rpsWinnerMatrix = [[-1,1,0],[1,-1,2],[0,2,-1]]
    
    while True:
        
        print()
        print("Rock, Paper, or Scissors?(Exit to quit)")
        print()
    
        userInput = input("your choice: ")
        
        if userInput.lower() == "exit":
            break
        elif userInput.lower() == "rock":
            userChoice = 0
        elif userInput.lower() == "paper":
            userChoice = 1
        elif userInput.lower() == "scissors":
            userChoice = 2
        else:
            print("incorrect input")
            continue
        
        aiChoice = random.randint(0, 2)
        
        print("Opponent chooses",rpsChoicesMap[aiChoice])
        
        winner = rpsWinnerMatrix[userChoice][aiChoice]
        
        if winner == userChoice:
            print("YOU WIN!")
        elif winner == aiChoice:
            print("YOU LOOSE!")
        else:
            print("ITS A TIE")
