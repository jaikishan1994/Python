# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 03:34:21 2018

@author: v-jaimo
"""

n = int(input())

dictionary = {}

for i in range(1,n+1):
    dictionary[i]= (i*i)
    
print(dictionary,end='') 
