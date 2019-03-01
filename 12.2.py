#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 11:56:07 2018

@author: sinsakuokazaki
"""

class Location:
    def __init__(self, row= 0, column = 0):
        self.row = row
        self.column = column
        self.maxValue = []
    
    def locateLargest(self, elements):
        valuemax = 0
        index = []
        for i in range(self.row):
            for j in range(self.column):
                if elements[i][j] > valuemax:
                    valuemax = elements[i][j]
                    index = [i, j]
        self.maxValue.append(valuemax)
        self.maxValue.append(index)
        return self.maxValue

    
def main():
    sizeInput = input("Enter the number of rows and columns in the list: ").split(",")
    row = int(sizeInput[0])
    column = int(sizeInput[1])
    
    elements = []
    for i in range(row):
        elements.append([ float(a) for a in input("Enter row: ").split()])
    
    location = Location(row, column)
    
    location.locateLargest(elements)
    
    print("The location of the largest element is ", location.maxValue[0], "at ", tuple(location.maxValue[1]))
    


main()

