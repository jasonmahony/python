#!/usr/bin/python

sentence = "Let's reverse this sentence."

def reversing(strings):
#    new = strings.split()
#    new.reverse()
#    return " ".join(new)
    return elem for elem in reversed(strings.split())
#    return " ".join(strings.split().reverse())
#    return ' '.join(strings.split()[::-1])
print reversing(sentence)

