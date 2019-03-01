# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#import math
import math

#initiate valuable
degreeList = []
sinList = []
cosList = []
sin = 0
cos = 0

#create lists of degree, sin, and cos
for i in range(0, 37):
    degreeList.append(i * 10)
    
    sin = math.sin(math.radians(degreeList[i]))
    sinList.append(round(sin, 4))
    
    cos = math.cos(math.radians(degreeList[i]))
    cosList.append(round(cos, 4))

#define function to print degree, sin, and cos
def desplay(degree, sin, cos):
    print(format(degree, "<10.4f"), format(sin, "<10.4f"), format(cos, "<10.4f"))

#print  columns name
print(format("Degree", "<10s"), format("Sin", "<10s"), format("Cos", "<10s"), "\n")

#print degrees, sins, and coses
for i in range(0, 37):
    desplay(degreeList[i], sinList[i], cosList[i])
    