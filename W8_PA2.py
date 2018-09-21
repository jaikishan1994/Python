# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math

n = int(input())


def sum_individuals(n):
    su= 0
    while(n):
        su = su + n%10
        n = math.floor(n/10)
    return su

s = sum_individuals(n)
while(s > 9):
    s = sum_individuals(s)
print(s,end="")

    