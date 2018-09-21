# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 04:12:40 2018

@author: v-jaimo
"""

def printDict():
    print(dictionary,end='') 

n = int(input())
dictionary = {}

for i in range(1,n+1):
    dictionary[i]= (i*i)

printDict()

