#!/usr/bin/python

import random

number = random.randint(1, 9)
guess = None

while (guess != number):
    guess = raw_input('Guess a number between 1 and 9 or "exit" to end the game: ')
    if guess == "exit":
        print "Ending the game..."
        break
    guess = int(guess)
    if guess > number:
        print "Too high."
    elif guess < number:
        print "Too low."
    else:
        print "You're right!"