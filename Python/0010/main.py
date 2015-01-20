# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 11:10:56 2014

@author: MasterMac
"""

def  hannoi( n, A, B, C ):
    if n == 1:
        print 'Move', n, 'from', A, 'to', C
    else:
        hannoi( n-1, A, C, B )
        print 'Move', n, 'from', A, 'to', C
        hannoi( n-1, B, A, C )

n = int(raw_input())
hannoi( n, 'A', 'B', 'C' )
