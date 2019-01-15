#!/usr/bin/python

#https://www.codewars.com/kata/balanced-number-special-numbers-series-number-1/train/python

def balanced_num(number):
    lst = list(str(number))
    digits = len(lst)
    if int(len(lst)) < 2:
        return "Balanced"
    else:
        if len(lst) % 2 == 0:
            middle = int(len(lst)) / 2
            sum_left = sum(list(map(int, lst[0: middle - 1])))
            sum_right = sum(list(map(int, lst[middle + 1: -1])))
            return "Balanced" if sum_left == sum_right else "Not Balanced"
#            sum_left = map(lambda x: sum(int(x)), lst[0: middle - 1])
#            return sum_left
            #sum_left = map(lambda x: sum(x), index[0: middle - 1])
            #sum_right = sum(index) - sum_left - sum_mid
            #return "Balanced" if sum_right == sum_left else "Not Balanced"
        else:
            middle = (int(len(lst)) - 1) / 2
            sum_left = sum(list(map(int, lst[0: middle])))
            sum_right = sum(list(map(int, lst[middle + 1: -1])))
            return "Balanced" if sum_left == sum_right else "Not Balanced"

print balanced_num(35335)
print balanced_num(7935)
print balanced_num(79358909)