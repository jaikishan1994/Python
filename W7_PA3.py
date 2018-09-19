# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 18:02:13 2018

@author: Kish
"""

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


while(top<=bottom and left<=right):
    #iterate the left column
    for i in range(top,bottom+1):
        print(matrix[i][left],end= " ")
    left +=1
    
    #iterate the bottom row
    for i in range(left,right+1):
        print(matrix[bottom][i],end=' ')
    bottom -= 1
    
    #iterate the right column
    for i in range(bottom,top-1,-1):
        print(matrix[i][right],end=' ')
    right -= 1
    
    #iterate the top row
    for i in range(right,left-1,-1):
        print(matrix[top][i],end=' ')
    top += 1
