#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 15:35:57 2018

@author: sinsakuokazaki
"""

#input number for line
number = int(input("Enter the number of lines:"))
#configurate integer range
if type(number) == int and number >= 1 and number <= 15:
    #print pyramid
    for i in range(1, number + 1):
        for j in range(number + 1 - i):
            print(" ", end = "  ")
        for j in range(i, 0, -1):
            print(j, end = "  ")
        if i == 1 :
            print("\n")
        else: 
            for k in range(2, i+1):
                print(k, end = "  ")
            print("\n")