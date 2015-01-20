# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 11:10:56 2014

@author: MasterMac
"""
import math
a = float(raw_input())
b = float(raw_input())
c = float(raw_input())

cosC = (a**2 + b**2 - c**2)/(2.0 * a * b)
print round(math.degrees(math.acos(cosC)), 1)
