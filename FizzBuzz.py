# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 07:29:04 2018

@author: v-jaimo
"""

#Fizz_Buzz 
#For multiples of 3 -- Fizz
#for multiples of 5 -- Buzz
#For multiples of 3 & 5 -- Fizz Buzz

for i in range(1, 101, 1):
    if((i%3 == 0)&(i%5 == 0)):
        print(str(i),": Fizz Buzz")
        continue;
    else:
        if(i%3 == 0):
            print(str(i), ": Fizz");
            continue;
        if(i%5 == 0):
            print(str(i), ": Buzz");
            continue;
        else:
            print(str(i), ": -");


#Syntax of for loop in python
#for(start, end, step)
            
for i in range(100, 0, -1):
    if((i%3 == 0)&(i%5 == 0)):
        print(str(i),": Fizz Buzz")
        continue;
    else:
        if(i%3 == 0):
            print(str(i), ": Fizz");
            continue;
        if(i%5 == 0):
            print(str(i), ": Buzz");
            continue;
        else:
            print(str(i), ": -");
        
        
        
        
       
