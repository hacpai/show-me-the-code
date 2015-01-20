# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 11:10:56 2014

@author: MasterMac
"""

n = int(raw_input())
sum = 0

for i in range(n):
    if i % 3 == 0 or i % 5 == 0:
        sum += i

print sum
