#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 15:35:21 2018

@author: sinsakuokazaki
"""
#import math
import math
#define deviation function
def deviation(x):
    s = 0;
    for i in x:
        s += (i - mean(x)) ** 2
    return math.sqrt(s / (len(x) - 1))
    
#define mean function
def mean(x):
    s = 0
    for i in x:
        s += i
    return s / len(x)

#define test program 
def test():
    #enter numbers separated with space
    numbers = input("Enter numbers: ")
    num = [float(i) for i in numbers.split()]
    print("The mean is ", round(mean(num), 2))
    print("The standard deviation is ", round(deviation(num), 5))