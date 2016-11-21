#!/usr/bin/python

number = input("Enter a number: ")

def is_prime(x):
    span = range(2, x)
    for i in span:
        if x % i == 0:
            result = False
            break
        else:
            result = True
    return result

if is_prime(number) == True:
    print str(number) + " is a prime number"
else:
    print str(number) + " is not a prime number"