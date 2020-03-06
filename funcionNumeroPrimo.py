# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 19:20:54 2020

@author: CEC
"""

# Reto de funciones 
def isPrime(num):
    if num < 2:    
        return False
    for i in range(2, num): 
        if num % i == 0:    
            return False
    return True    

print(isPrime(29))
for i in range(1, 20):
	if isPrime(i + 1):
			print(i + 1, end=" ")

