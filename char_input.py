#!/usr/bin/python

import datetime

name = raw_input("What is your name? ")
age = input("Enter your age: ")

print("Hi " + name + "!")
print("You are " + str(age) + " years old.")

year = int(datetime.date.today().year)
togo = int(100 - age)

answ = int(year + togo)

print("You will be 100 year old in " + str(answ) + ".")