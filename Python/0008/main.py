# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 11:10:56 2014

@author: MasterMac
"""

def fib(n):
    s = 0
    f1, f2 = 1, 2 
    while f2 < n:
        if f2 % 2 == 0:
            s += f2
        f1, f2 = f2, f1 + f2
    return s

n = int(raw_input())

print fib(n)
