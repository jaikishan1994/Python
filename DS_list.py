# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 04:25:21 2018

@author: v-jaimo
"""

#list - [] 

shopping = [] # an empty list is created

for i in range(3):
    print(i)
    

'''
for item in shopping:
    print(item)
'''

shopping.append("Banana")
shopping.append("Mango")
shopping.append("Curd");

shopping.remove("Banana");

print(shopping)

shopping.insert(0, "Apple"); #insert at the custom location.

print(shopping);


Age_Students = [21,24,22,26,32,24,22,27,29,22,21,23,25,29,32,21]

Age_Students.count(21) #No.of students with age 21

len(Age_Students)

#Iterate the list
for student in range(len(Age_Students)):
    print(Age_Students[student])
#or    
print("\n or \n");
for student in Age_Students:
    print(student)
    
#slicing
    #SYNTAX: list_name[start:end+1]

print(Age_Students[1:4])

#default start index =0
#default last index = len(list)