#!/usr/bin/python

input = raw_input("Enter a string and I'll let you know if it's a palindrome: ")
reverse = input[::-1]

if input == reverse:
    print "Palindrome!"
else:
    print "Not a palindrome."