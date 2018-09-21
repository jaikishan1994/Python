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

bkp_s = int(s)
bkp_n = int(n)
bkp_m = int(m)

days = 0
if(n >= m):
    ans = 1
    while(n >= m and days!=s):
        n = n - m
        days += 1
        
        if(days%6 == 0):
            if(n < m):
                print("NO",end="")
                break;
        else:
            if(n < m):
                n = n + bkp_n
                ans += 1
            
        if(days == s):
            print(ans,end="")
            break;
else:
    print("NO",end="")
    