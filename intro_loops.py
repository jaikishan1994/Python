# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 01:58:49 2018

@author: v-jaimo
"""
'''
for i in range(10):
    print(i)
'''
'''
sum = 0;
x = "+";
for i in range(10):
    sum = sum + i;
    if(i==9):
        print(i,x,"=")
    else:
        x = i+x;
print(i,"+")
        
print(sum)

'''

'''
Multiplication table

x = input("What table would you like to display:   ");
for i in range(11):
    print(x," X ", i, "= ", int(x)*i)

'''
'''
choice = 1;
token = 1;
while(choice == 1):
    print("Token ",token," may come in!");
    choice = int(input("choice (0/1) ?"));
    token = token + 1;
'''
'''
a=0
for i in range(10):
    a=a+1;
    print(a);
    
print(a)
'''
'''
s1="IIT "  #Remember there is a space after T in IIT
s2="Punjab"
s1=s1*2
s2="Ropar"
print(s1,s2)

'''
n=5
if(n>1)
	print("Hello")