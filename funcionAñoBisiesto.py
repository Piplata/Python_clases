# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 20:15:39 2020

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
    
print(isYearLeap(2000))

testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
