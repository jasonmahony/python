#!/usr/bin/python

#https://www.codewars.com/kata/balanced-number-special-numbers-series-number-1/train/python

def balanced_num(number):
    lst = list(map(int, list(str(number))))
    if int(len(lst)) < 3:
        return "Balanced"
    else:
        if len(lst) % 2 == 0:
            middle = int(len(lst)) / 2
            sum_left = sum(lst[0: int(middle - 1)])
            sum_right = sum(lst[int(-middle + 1):])
        else:
            middle = (int(len(lst)) - 1) / 2
            sum_left = sum(lst[0: int(middle)])
            sum_right = sum(lst[int(-middle):])
        return "Balanced" if sum_left == sum_right else "Not Balanced"

print balanced_num(35335)
print balanced_num(7935)
print balanced_num(9966586996)
print balanced_num(66658902)