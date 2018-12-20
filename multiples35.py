#!/usr/bin/python

def solution(n):
  number = 0
  for num in range(1, n):
    if num % 3 == 0 or num % 5 == 0: number += num
  return number

print solution(23)
