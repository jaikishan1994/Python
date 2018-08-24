# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 03:16:14 2018

@author: v-jaimo
"""

n = int(input())
fact = 1
for i in range(1, n+1, 1):
    fact = fact * i
print(fact,end='')
    