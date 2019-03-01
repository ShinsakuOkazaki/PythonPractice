#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 12:35:03 2018

@author: sinsakuokazaki
"""

#input celsius and covert string into integer
celsius = int(input("Enter a degree in Celsius: "))

#calculate fahrenheit
fahrenheit = (9 / 5) * celsius + 32

#print the result
print(celsius, "Celsius is", fahrenheit, "Fahrenheit")