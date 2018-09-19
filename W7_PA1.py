# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 17:47:45 2018

@author: Kish
"""

n = int(input())

for i in range(1,n+1):
    for j in range(1,i+1):
        if(j==i):
            print(j,end = "")
        else:
            print(j,end = " ")
    if(i==n):
        print(end='')
    else:
        print(end='\n')
    