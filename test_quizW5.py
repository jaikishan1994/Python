# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 04:21:32 2018

@author: v-jaimo
"""
a =  [25,10,40,70,100]

for i in range( len(a) ):
    for j in range(i+1, len (a) ):
        if a[ i ]<a[ j ]:
            a[ i ] , a[ j ]=a[ j ] , a[ i ]

