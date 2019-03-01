#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 16:42:59 2018

@author: sinsakuokazaki
"""
#import math
import math

#input number of sides and length of side
n = int(input("Enter the number of sides: "))
s = float(input("Enter the side: "))

#calculate area of polygon
area = (n * s ** 2) / (4 * math.tan(math.pi / n))

#print the result
print("The area of the polygon is", area)