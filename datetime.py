# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 05:34:31 2018

@author: v-jaimo
"""

# Birthday Paradox

import random
import datetime

year = random.randomint(1890,2017)

datetime.date.today().strftime("%Y") #year
datetime.date.today().strftime("%y") #year last two digits
datetime.date.today().strftime("%m") #Month number like 01,02,03....12
datetime.date.today().strftime("%D") #Date id mm/dd/yy format
datetime.date.today().strftime("%h") or "%b" #Month name like Jan,Feb,..
datetime.date.today().strftime("%d") #dd
datetime.date.today().strftime("%a") #Week name like Mon,Tue,Wed,..
datetime.date.today().strftime("%A") #Week name like Monday,Tuesday,..



