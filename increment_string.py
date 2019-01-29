#!/usr/bin/python

def increment_string(strng):
    lst = list(strng)
    if not lst or lst[-1].isdigit() == False:
        return strng + "1"
    elif strng.isdigit():
        return str(int(strng) + 1).zfill(len(lst))
    else:
        digit = []
        while lst[-1].isdigit():
            digit.append(lst.pop())
        digit.reverse()
        lst.append(str(int(''.join(digit)) + 1).zfill(len(digit)))
        return ''.join(lst)

print increment_string("foobar00")
print increment_string("")
print increment_string("foobar099")