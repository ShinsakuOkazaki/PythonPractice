#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 10:35:28 2018

@author: sinsakuokazaki
"""
import math

class Geometric:
    def __init__(self, color = 'green', filled = True):
        self.__color = color
        self.__filled = filled
    
    def getColor(self):
        return self.__color
    
    def setColor(self, color):
        self.__color = color
    
    def isFilled(self):
        return self.__filled
    
    def setFilled(self, filled):
        self.__filled = filled
    
    def __str__(self):
        return "color: " + self.__color + "and filled: " + str(self.__filled)
    
class Triangle(Geometric):
    def __init__(self, side1 = 1.0, side2 = 1.0, side3 = 1.0):
        super().__init__()
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3
        
    def getSide1(self):
        return self.__side1
    
    def getSide2(self):
        return self.side2
    
    def getSide3(self):
        return self.__side3
    
    def getArea(self):
        s = (self.__side1 + self.__side2 + self.__side3) / 2
        area = math.sqrt(s * (s - self.__side1) * (s - self.__side2) * (s - self.__side3))
        
        return area
    
    def getPerimeter(self):
        perimeter = self.__side1 + self.__side2 + self.__side3
        
        return perimeter
    
    def __str__(self):
        return "Triangle: side1 = " + str(self.__side1) + \
        " side2 = " + str(self.__side2) +\
        " side3 + " + str(self.__side3)
        
    
    
def main():
    sidesInput = input("Enter length of the three sides: ").split(",")
    for i in range(len(sidesInput)):
        sidesInput[i] = int(sidesInput[i])

    colorInput = input("Enter the color: ")
    filledInput = input("Enter 1 if the triangle is filled, otherwise enter 0: ")
    if filledInput == "1":
        filledInput = True
    elif filledInput == "0":
        filledInput = False

    triangle = Triangle(sidesInput[0], sidesInput[1], sidesInput[2])
    triangle.setColor(colorInput)
    triangle.setFilled(filledInput)
    
    print("The area is ", triangle.getArea())
    print("The perimeter is ", triangle.getPerimeter())
    print("The color is ", triangle.getColor())
    print("Is the triangle filled? ", triangle.isFilled())    
    
main()