# -*- coding: utf-8 -*-
"""
Created on Tue May 11 18:59:28 2021

@author: Zachery Van Es
"""

def hangman():
    hangmanword = "longtest"
    guesses = ""
    turns = 10
    intro = "Your word is {} spaces long, you have 10 tries to guess it"
    print(intro.format(len(hangmanword)))
    while turns > 0:
        failed = 0
        for char in hangmanword:
            if char in guesses:
                print (char,end='')
            else:
                print("_",end='')
                failed += 1
        if failed == 0:
            print("\nYou win!")
            break
        
        guess = ""
        while(len(guess)!= 1):
            guess = input("Guess letter of word: ")
            if len(guess)!=1:
                print("Only one character allowed")
        
        guesses += guess
        
        if guess not in hangmanword:
            turns -= 1
            print("incorrect guess")
            turnnumber = "you have {} number of guesses left!"
            print(turnnumber.format(turns))
        if (turns == 0):
            print("GAME OVER!")
            
if __name__ == "__main__":
    hangman()