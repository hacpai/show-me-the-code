# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 11:10:56 2014

@author: MasterMac
"""

START_DAY_FOR_JAN_1_1800 = 3

def IsLeap( year ):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

def GetNumOfDaysInMonth( year, month ):
    if month in ( 1, 3, 5, 7, 8, 10, 12 ):
        return 31
    elif month in ( 4, 6, 9, 11 ):
        return 30
    elif IsLeap( year ) == True:
        return 29
    else:
        return 28

def GetTotalNumOfDay( year, month ):
    days = 0
    for y in range( 1800, year ):
        if IsLeap == True:
            days += 366
        else:
            days += 365

    for m in range( 1, month+1 ):
        days += GetNumOfDaysInMonth( year, m )
    
    return days

def GetEndDay( year, month ):
    return ( START_DAY_FOR_JAN_1_1800 + GetTotalNumOfDay( year, month )) % 7

year = int( raw_input() )
month = int( raw_input() )

print GetEndDay( year, month )
