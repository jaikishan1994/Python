# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 01:54:26 2018

@author: v-jaimo
"""

list_1 = [];
for i in range(1,51,1):
    list_1.append(i);

#a, b = input().split(',')    #Input two numbers at once with , seperated

a, b = input().split()    #Input two numbers at once seperated with a white space

a = int(a)
b = int(b)

for item in list_1[a:b]:
    print(item);

#print(list_1[a:b])

