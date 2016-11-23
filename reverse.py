#!/usr/bin/python

string = "You this needs to be reversed."

def rorder(string):
    return " ".join(reversed(string.split()))

print rorder(string)