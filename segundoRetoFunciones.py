# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 19:58:23 2020

@author: CEC
"""

def l100kmtompg(litros):
    x = (litros/100000)*(1/3.785411784)*1.609344
    return x

def mpgtol100km(miles):
    y = (miles*1609.344 )/1
    return y

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))

    
    