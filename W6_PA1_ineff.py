# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 23:47:44 2018

@author: v-jaimo
"""

l = []
k = input()
l = k.split(' ')

#iterate the loop to delete the duplicates
k = len(l)
i = 0
while(i < k):
    j = i+1
    while(j < k):
        if(l[i]==l[j]):
            l.pop(j)
            k = len(l)
            continue;
        j += 1
    i += 1

#print the list after removing duplicates
for i in range(0,len(l)):
    if(i==(len(l)-1)):
        print(l[i],end="")
    else:
        print(l[i],end=" ")
        