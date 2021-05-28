def odd_or_even(arr):
    sum = 0
    for elem in arr:
        sum += elem
    return True if sum % 2 == 0 else False

print(odd_or_even([1023, 1, 2]))