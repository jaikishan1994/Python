# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 18:08:36 2018

@author: Kish
"""

matrix = []

n = int(input())

for i in range(n):
    row = input().split(' ')
    matrix.append(row)

for i in range(0,n):
    for j in range(0,n):
        matrix[i][j]=int(matrix[i][j])

top = 0
bottom = n-1
left = 0
right = n-1


while(top<bottom and left<right):
    
    prev = matrix[top+1][left]
    #iterate the top row
    for i in range(left,right+1):
        matrix[top][i],prev = prev,matrix[top][i]
    top += 1
    
    #iterate the right column
    for i in range(top,bottom+1):
        matrix[i][right],prev = prev, matrix[i][right]
    right -= 1
    
    #iterate the bottom row
    for i in range(right,left-1,-1):
        matrix[bottom][i],prev = prev,matrix[bottom][i]
    bottom -= 1
    
    #iterate the left column
    for i in range(bottom,top-1,-1):
        matrix[i][left],prev = prev, matrix[i][left]
    left +=1

for i in range(0,n):
    for j in range(0,n):
        matrix[i][j]=int(matrix[i][j])
        if(j == n-1):
            print(matrix[i][j],end="")
        else:
            print(matrix[i][j],end=" ")
    if(i == n-1):
        print("",end = "")
    else:
        print("")
