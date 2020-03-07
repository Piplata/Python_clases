# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 10:50:35 2020

@author: CEC
"""

file = open("devices.txt","r")
for item in file :
    print(item)
file.close()