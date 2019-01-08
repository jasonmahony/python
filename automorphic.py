#!/usr/bin/python

import array

def automorphic(n):
    return "Automorphic" if list(str(n**2))[-len(str(n)):] == list(str(n)) else "Not!!"

print automorphic(25)
