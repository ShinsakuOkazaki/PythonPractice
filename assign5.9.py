#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 15:12:43 2018

@author: sinsakuokazaki
"""

tuition = 10000

increaseRate = 1.05

for i in range(0, 11):
    tuition = tuition * increaseRate 
    
tuitionTotal = tuition

for i in range(0, 5):
    tuitionTotal += tuitionTotal * increaseRate
    

print("The tuition in ten years is $", end = "")
print(format(tuition, ".2f"))
print("The total cost of four years' wirth of tuition starting ten years from now is $", end="")
print(format(tuitionTotal, ".2f"))