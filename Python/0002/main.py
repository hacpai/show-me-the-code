# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 11:10:56 2014

@author: MasterMac
"""

sec = int(raw_input())

hour = sec / 60**2 
minute = sec / 60 % 60
second = sec % 60

print hour, minute, second
