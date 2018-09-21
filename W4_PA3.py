# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 03:22:34 2018

@author: v-jaimo
"""
import random

noe = int(input())
list = []

for i in range(noe):
    c = int(input())
    list.append(c)

sorted = list.copy()
sorted.sort()

while(sorted != list):
    i = random.randint(0,len(list)-1)
    j = random.randint(0,len(list)-1)
    list[i],list[j]= list[j],list[i]
    
    if(sorted == list):
        print(*list,sep =" ",end='')
        break;
