# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 11:10:56 2014

@author: MasterMac
"""

import math

def IsPrime (n):
    for i in range(2, int( math.sqrt(n) ) + 1):
        if n % i == 0:
            return False
    return True

num = int(raw_input())
count = 0
for i in range(2, num):
    isPrime = IsPrime(i)
    if isPrime:
        num_t1 = num_t2 = num_t3 = i 
        c = 0 
        num_t1 /= 10
        c += 1
        while num_t1 > 0 :
            num_t1 /= 10
            c += 1
        while num_t2 != 0 :
            num_t3 = num_t3 / 10 + (num_t3 % 10) * (10 ** (c - 1))
            num_t2 /= 10
            if IsPrime(num_t3) == False:
                break
        else:
            count += 1

print count
