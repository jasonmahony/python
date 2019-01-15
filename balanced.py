#!/usr/bin/python

def balanced_num(number):
    digits = len(str(number))
    if int(digits) < 2:
        return "Balanced"
    else:
        index = list(str(number))
        if digits % 2 == 0:
            middle = int(digits) / 2
            sum_mid = index[middle - 1] + index[middle]
            #sum_left = map(lambda x: sum(x), index[0: middle - 1])
            #sum_right = sum(index) - sum_left - sum_mid
            #return "Balanced" if sum_right == sum_left else "Not Balanced"
        else:
            middle = (int(digits) - 1) / 2
            return index[middle]
            
print balanced_num(795)