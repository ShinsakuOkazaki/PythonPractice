#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 00:09:35 2018

@author: sinsakuokazaki
"""

class Rectangle:
    
    def __init__(self, length = 1, wide = 1):
        self.length = length
        self.wide = wide
        
    def getPerimeter(self):
        return 2 * self.length + 2 * self.wide
    
    def getArea(self):
        return self.length * self.wide
    
    def setLengthAndWide(self, length, wide):
        self.length = length
        self.wide = wide
