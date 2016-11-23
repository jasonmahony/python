#!/usr/bin/python

string = "You this needs to be reversed."

def rorder(string):
    return " ".join(string.split()[::-1])
#    return " ".join(reversed(string.split()))

print rorder(string)
