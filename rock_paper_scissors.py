#!/usr/bin/python

import random

while (quit != "q"):
    user = raw_input('Let\'s start the game!\nType in "Rock", "Paper" or "Scissors": ')
    comp = random.choice(["Rock", "Paper", "Scissors"])
    if user == comp:
        print ("Tie!\nThe computer had " + comp)
    elif user == "Rock" and comp == "Scissors" or user == "Scissors" and comp == "Paper" or user == "Paper" and comp == "Rock":
        print ("You win!!\nYou beat the computer's " + comp)
    else:
        print ("You lose..\nThe computer had " + comp)
    quit = raw_input('Type "q" to quit or Enter to keep playing: ')