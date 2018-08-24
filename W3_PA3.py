# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 02:12:19 2018

@author: v-jaimo
"""

list_1 = [];
for i in range(1,51,1):
    list_1.append(i);
    
div = int(input());

count = 0;

for i in list_1:
    if(list_1[i-1]%div == 0):
        count = count + 1;

print(count-1);

        