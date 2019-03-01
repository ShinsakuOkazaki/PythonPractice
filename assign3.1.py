#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 13:33:16 2018

@author: sinsakuokazaki
"""
#import math
import math

#input length from the cnter to a vertex
r = float(input("Enter the length from the center to a vertex: "))

#calculate s
s = 2 * r * math.sin( math.pi / 5)

#calculate area
area = 3 * math.sqrt(3) / 2 * s ** 2

#print result
print("The area of the pentagon is", round(area, 2))