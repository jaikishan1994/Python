# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 07:04:19 2018

@author: v-jaimo
"""
'''
N – Maximum unit of food you can buy each day.
S – Number of days you are required to survive.
M – Unit of food required each day to survive.

input order should be S, N, M
'''

s,n,m = input().split(' ')


s = int(s)
n = int(n)
m = int(m)

#bkp_s = int(s)
bkp_n = int(n)
#bkp_m = int(m)

if(s > 0 and n >= m):
    pkt = 1
    days = 1
    while(1):
        if(n < m):
            if((days)%7 == 0):
                print("NO",end="")
                break;
            else:
                n = n + bkp_n
                pkt += 1
        
        n = n - m
        
        if(days == s):
            print(pkt,end="")
            break;
        days += 1
else:
    print("NO",end="")