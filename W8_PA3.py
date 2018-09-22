# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 06:14:33 2018

Programming Assignment 3: Push

@author: v-jaimo
"""
zeros = 0
l = input().split(' ')

for i in range(0,len(l)):
    l[i]= int(l[i])

i = 0
length = len(l)
while(i < length):
    if(l[i] == 0):
        zeros += 1
        del(l[i])
        length = len(l)
    i += 1

for i in range(0,zeros):
    l.append(0)

for i in range(0,len(l)):
    if(i != len(l)-1):
        print(l[i],end=" ")
    else:
        print(l[i],end="")
    

