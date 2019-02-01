#!/usr/bin/python

import string

def high(x):
    values = dict()
    for index, letter in enumerate(string.ascii_lowercase):
       values[letter] = index + 1
    words = x.split()
    score_card = list()
    for word in words:
        word_score = 0
        for c in list(word):
            word_score = word_score + values[c]
        score_card.append(word_score)
    return words[score_card.index(max(score_card))]

    
print high('man i need a taxi up to ubud')
print high('what time are we climbing up the volcano')

##### Rules
#Given a string of words, you need to find the highest scoring word.
#Each letter of a word scores points according to it's position in the alphabet: a = 1, b = 2, c = 3 etc.
#You need to return the highest scoring word as a string.