#!/usr/bin/python

from fractions import gcd

def sum_fracts(lst):
    if lst == []: return None
    numer = 0
    denom = 1
    for n in lst:
        denom = int(n[1])*denom
    for m in lst:
        numer = int(m[0])*denom // m[1] + numer
    d = gcd(numer, denom)
    if d == denom:
        return numer/denom
    elif d != 0:
        return [numer//d,denom//d]
    else:
        return [numer, denom]

print sum_fracts([[1, 2], [1, 3], [1, 4]])
print sum_fracts([[1, 3], [5, 3]])
print sum_fracts([])