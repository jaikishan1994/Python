# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 12:10:24 2018

@author: Kish
"""

size = int(input())
matrix = [[0]*size]*size

for i in range(0,size):
        matrix[i] = input().split(' ')

for i in range(0,size):
    for j in range(0,size):
        if(i < j):
            matrix[i][j] = 0

for i in range(0,size):
    for j in range(0,size):
        matrix[i][j]=int(matrix[i][j])
        if(j == size-1):
            print(matrix[i][j],end="")
        else:
            print(matrix[i][j],end=" ")
    if(i == size-1):
        print("",end = "")
    else:
        print("")
