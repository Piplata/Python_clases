# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 15:40:52 2019

@author: Juan Carlos
"""

class JustCounter:
   __secretCount = 0
  
   def count(self):
      self.__secretCount += 1
      print (self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
#print (counter.__secretCount)
print(counter._JustCounter__secretCount)