# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 09:19:29 2020

@author: CEC
"""

class Employee:
    'Common base class for all employees'
    empCount = 0 
    def __init__(self,name,salary ): #Metodo Constructor, siempre con self como practica de programador
        self.name = name;
        self.salary = salary
        Employee.empCount +=1
    def displayCount(self):
        print("Total Employee %d" %Employee.empCount)
    def displayEmployee(self):
        print("Name: ", self.name, ",Salary:", self.salary)

emp1 = Employee("Zara",2000)
emp2 = Employee("Steven", 50000)
emp3 = Employee("Juan", 2500)
emp4 = Employee("Diana", 1000)

emp1.displayEmployee()
emp2.displayEmployee()

emp1.displayCount()