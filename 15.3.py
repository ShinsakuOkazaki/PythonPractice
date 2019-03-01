#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 00:03:06 2018

@author: sinsakuokazaki
"""

def gcd(m,n):
    if m % n == 0:
        return n
    
    return gcd(n, m % n)


def main():
    numbersInput = input("Enter two integers: ").split(",")
    for i in range(len(numbersInput)):
        numbersInput[i] = int(numbersInput[i])
        
    m = numbersInput[0]
    n = numbersInput[1]
    
    print("The greatest common divisor using is: ", gcd(m,n))
    
main()