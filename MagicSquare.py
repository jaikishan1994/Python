# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math

# Magic Square 3

def magicSquare(n):
    
    
    #Create a nXn 2-D array initialize with 0
    for i in range(n):
        l = []              #Create a list for each row
        for j in range(n):
            l.append(0)         #Append the column values for that row... Build up the row
        MagicSquare.append(l)   #Append this row to the MagicSquare

def computePosition(P,Q,n):
    test = 1
    while(test):
            if((P == -1) & (Q == n)):
                P = 0
                Q = n-2
            if(P == -1):
                P = n-1
            if(Q == n):
                Q = 0
            if(MagicSquare[P][Q] != 0):
                Q = Q-2
                P = P+1
            if(MagicSquare[P][Q] == 0):
                test = 0
    return P,Q
            
'''
Magic Square rules:
1. Position of 1 is always (n/2,n-1)
2. Assume the previous positions as P = n/2, Q = n-1
3. Next number's position will be (P-1, Q+1)
    if P == -1 and Q == n then make (P=0, Q=n-2)
4. if P == -1 then P = n-1
5. if Q == n then Q = 0
6. If an element is already present in (P,Q) then make it (P+1,Q-2)
'''

#Positions 
n = int(input("Magic Square Number?  "))
P = math.floor(n/2)
Q = n-1

MagicSquare = []
#Initialize magic square
magicSquare(n);

MagicSquare[P][Q] = 1

for i in range(2, n*n+1, 1):
    P = P-1;
    Q = Q+1;
    P,Q = computePosition(P,Q,n)
    MagicSquare[P][Q] = i





        
            
        