# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 18:45:56 2020

@author: CEC
"""

def address(street,city,postalCode):
    print('Your addressis:',street, 'St',city, 'y su codigo postal es:',postalCode)

s= input('Street: ')
pc = input('Postal Code:')
c = input('City:')

address(s,c,pc)