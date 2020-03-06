# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 09:39:42 2020

@author: CEC
"""
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()