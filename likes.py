#!/usr/bin/python

def likes(names):
    num = len(names)
    if num < 2:
        per = names[0] if num == 1 else "no one"
        return per + " likes this"
    if num == 2:
        ppl = names[0] + " and " + names[1]
        return ppl + " like this"
    if num > 2:
        f2 = ', '.join(names[:2])
        ppl = f2 + " and " + names[2] if num == 3 else f2 + " and " + str(num - 2) + " others"
        return ppl + " like this"

print likes(["Alex", "Jacob", "Mark", "Max"])
print likes(["Alex", "Jacob", "Max"])
print likes(["Alex", "Jacob"])
print likes(["Jason"])
print likes([])
