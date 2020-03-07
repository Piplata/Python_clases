# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 10:57:40 2020

@author: CEC
"""

file = open("devices.txt","a")
while True:
    newItem = input('Enter a new a new devices: ')
    if newItem == "exit":
        print('All done')
        break
    else: 
        file.write(newItem + "\n")    
file.close()
        
