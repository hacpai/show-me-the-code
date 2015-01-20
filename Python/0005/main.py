# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 11:10:56 2014

@author: MasterMac
"""
import math

n = int(raw_input())
sum = 0
count = 2 

while count < n:
    for i in range(2, int(math.sqrt(count)) + 1):
        if count % i == 0:
            break
    else:
        sum += count 
    count += 1

print sum
