#!/usr/bin/python

import string
import random

charlen = input("Enter how many characters you want in your password: ")

chars = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passwd = random.sample(list(chars), charlen)
print "".join(passwd)