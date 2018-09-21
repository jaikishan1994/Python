# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 03:43:24 2018

@author: v-jaimo
"""
import math
# x,y axis initializing
x = 0   
y = 0

n = int(input())    #number of directions to be given
steps = [0]*n
for i in range(0,n):
    steps[i]= input()
    split = steps[i].rsplit()
    if(split[0] == "UP"):
        y += int(split[1])
    elif(split[0] == "DOWN"):
        y -= int(split[1])
    if(split[0] == "LEFT"):
        x += int(split[1])
    if(split[0] == "RIGHT"):
        x -= int(split[1])


distance = round(math.sqrt((x*x)+(y*y)))

print(distance,end='')