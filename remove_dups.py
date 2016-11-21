#!/usr/bin/python

array = ["j", "j", "jason", "jason", "julie", 3, 4, 4, 4, 2, 3]

def remove_dups(l):
    return list(set(l))
    
print remove_dups(array)