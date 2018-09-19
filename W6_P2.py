# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 12:06:41 2018

@author: Kish
"""

n = int(input())

while(n):
    if(n==2):
        print("YES",end="")
        break;
    elif(n%2==0):
        n = n/2
    else:
        print("NO",end="")
        break;
    