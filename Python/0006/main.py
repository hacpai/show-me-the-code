# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 11:10:56 2014

@author: MasterMac
"""

days = 1 
count = 0
"""
Jan = Mar = May = July = Aug = Otc = Dec = 31
Apr = Jum = Sep = Nov = 30
Feb1 = 28
Feb2 = 29
"""
month_31 = 31
month_30 = 30

for i in range(1900, 2001):
    if ((i % 4 and not i % 100) or (i % 400) ):
        month_Feb = 29
    else:
        month_Feb = 28
    for month in range(1, 13):
        if month == 2:
            days += month_Feb
        elif (month == 1) or (month == 3) or (month == 5) or (month == 7) or (month == 8) or (month == 10) or (month == 12):
            days += month_31
        else:
            days += month_30
        if days % 7 == 0 and i > 1900:
            count += 1

print count
