# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 02:06:41 2018

@author: v-jaimo
"""
r,c = input().split(' ')

r = int(r)
c = int(c)

array = []
ele = 1
col = 1
for i in range(r):
    col = 1
    row = []
    while((col <= c) & (ele <= r*c)):
        col += 1
        row.append(ele)
        ele += 1
    array.append(row)

for i in range(r):
    for j in range(c):
        if(j == c-1):
            print(array[i][j],end='')
        else:
            print(array[i][j],end=' ')
    if(i != r-1):
        print(end='\n')
        
        
