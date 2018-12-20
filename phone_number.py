#!/usr/bin/python

array = [0,1,2,3,4,5,6,7,8,9]

def create_phone_number(n):
    n.insert(6,"-")
    n.insert(3," ")
    n.insert(3,")")
    n.insert(0,"(")
    number = "".join(map(str, array))
    print number

create_phone_number(array)
