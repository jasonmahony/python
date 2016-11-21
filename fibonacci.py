#!/usr/bin/python

def fib(limit):
    i = 0
    while limit > 1:
        if i == 0:
            result = [1, 1]
            i += 1
        else:
            result.append(result[i] + result[i - 1])
            i += 1
        limit -= 1
    return result

print fib(345)
