#!/usr/bin/python

import string

def high(x):
    values = dict()
    for index, letter in enumerate(string.ascii_lowercase):
       values[letter] = index + 1
    words = x.split()
    word_list = list(enumerate(words))
    for word in words:
        word_score = 0
        for l in list(word):
            word_score = word_score + values[l]

    ##    word_score = reduce((lambda l, m: values[l] + values[m]), list(word))


    
print high('man i need a taxi up to ubud')
print high('what time are we climbing up the volcano')