# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 23:47:44 2018

@author: v-jaimo
"""

dict_count = {}

l = []
k = input()
l = k.split(' ')
for i in range(0,len(l)):
    dict_count[l[i]]=l.count(l[i])

l.sort()
k = len(l)    
i = 0

#iterate the loop to delete the duplicates
while(i < k):
    count = dict_count[l[i]]
    if(count > 1):
        for j in range(i+1,i+count):
            l.remove(l[i+1])
    k = len(l)
    i += 1;

#print the list after removing duplicates
for i in range(0,len(l)):
    print(l[i],end=" ")
   
