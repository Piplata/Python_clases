# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 20:50:36 2020

@author: CEC
"""

def isYearLeap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True 
            else:
                return False 
        else:
            return True
    else:
        return False
    
def daysInMonth(year,month):
	if year < 1900 or month < 1 or month > 12:
		return None
	days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	res  = days[month-1]
	if month == 2 and isYearLeap(year):
		res = 29
	return res
print(daysInMonth(2005,2))
    

    
