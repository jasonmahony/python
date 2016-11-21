#!/usr/bin/python

import random

a = random.sample(range(1, 100), 15)
b = random.sample(range(1, 100), 15)

c = [elem for elem in set(a) if elem in set(b)]