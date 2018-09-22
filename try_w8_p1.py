# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 05:25:04 2018

@author: v-jaimo
"""

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

def check(n,m,s,days,pkt):
    if((days+1)%7 == 0):
        if(n < m):
            print("NO",end="")
            return 0;
    else:
        if(n < m):
            n = n + bkp_n
            pkt += 1
    if(days == s):
        print(pkt,end="")
        return 0;


s = int(s)
n = int(n)
m = int(m)

bkp_s = int(s)
bkp_n = int(n)
bkp_m = int(m)

days = 0
pkt = 0
if(n>=m):
    while(n >= m and days!=s):
        days += 1
        n = n - m
        pkt = 1
        val = check(n,m,s,days,pkt)
        if(val == 0):
            break;
else:
    print("NO",end="")
