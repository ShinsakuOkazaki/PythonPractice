#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 15:56:53 2018

@author: sinsakuokazaki
"""

def sumDigits(n):
    if n == 0:
        return 0
    
    return n % 10 + sumDigits(n // 10)

def main():
    numberInput = int(input("Enter a integer: "))
    print("The sum of the digits in the integer is: ", sumDigits(numberInput))
    
main()