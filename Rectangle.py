#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 00:09:35 2018

@author: sinsakuokazaki
"""

class Rectangle:
    
    def __init__(self, width = 1, height = 2):
        self.width = width
        self.height = height
    
    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height
        
    def getPerimeter(self):
        return 2 * self.width + 2 * self.height
    
    def getArea(self):
        return self.width * self.height
    

def main():
    rect1 = Rectangle(4, 40)
    rect2 = Rectangle(3.5, 35.7)
    
    
    width1 = rect1.getWidth()
    height1 = rect1.getHeight()
    
    width2 = rect2.getWidth()
    height2 = rect2.getHeight()
    
    area1 = rect1.getArea()
    area2 = rect2.getArea()
    
    perimeter1 = rect1.getPerimeter()
    perimeter2 = rect2.getPerimeter()
    
    print("The width of rectangle1 is: ", width1)
    print("The height of rectangle1 is: ", height1)
    print("The area of rectangle1 is: ", area1)
    print("The perimeter of rectangle1 is: ", perimeter1, end ="\n\n")

    print("The width of rectangle2 is: ", width2)
    print("The height of rectangle2 is: ", height2)
    print("The area of rectangle2 is: ", area2)
    print("The perimeter of rectangle2 is: ", perimeter2, end ="\n\n")
    
    
main()

    
    
    