#!/usr/bin/python

# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.

def sort_last(tuples):
    def key(a):
        return a[-1]
    result = sorted(map(lambda t: [key(t), t], tuples))
    return map(lambda x: x[1] , result)

print sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])